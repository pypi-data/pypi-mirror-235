"""
Copyright 2019-2022 Lummetry.AI (Knowledge Investment Group SRL). All Rights Reserved.


* NOTICE:  All information contained herein is, and remains
* the property of Knowledge Investment Group SRL.  
* The intellectual and technical concepts contained
* herein are proprietary to Knowledge Investment Group SRL
* and may be covered by Romanian and Foreign Patents,
* patents in process, and are protected by trade secret or copyright law.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from Knowledge Investment Group SRL.


@copyright: Lummetry.AI
@author: Lummetry.AI
@project: 
@description:
  
TODO:
  implement config validation and base config format
  
"""

# PAHO

from collections import OrderedDict, deque

from select import select
from time import sleep

import paho.mqtt.client as mqtt
import traceback

from ..const import COLORS, COMMS, BASE_CT, PAYLOAD_CT


class MQTTWrapper(object):
  def __init__(self,
               log,
               config,
               recv_buff=None,
               send_channel_name=None,
               recv_channel_name=None,
               comm_type=None,
               on_message=None,
               post_default_on_message=None,  # callback that gets called after custom or default rcv callback
               debug_errors=False,
               connection_name='MqttWrapper',
               **kwargs):
    self.log = log
    self._config = config
    self._recv_buff = recv_buff
    self._mqttc = None
    self.debug_errors = debug_errors
    self._thread_name = None
    self.connected = False
    self.disconnected = False
    self._send_to = None
    self._nr_full_retries = 0
    self.__nr_dropped_messages = 0
    self._comm_type = comm_type
    self.send_channel_name = send_channel_name
    self.recv_channel_name = recv_channel_name
    self._disconnected_log = deque(maxlen=10)
    self._disconnected_counter = 0
    self._custom_on_message = on_message
    self._post_default_on_message = post_default_on_message
    self._connection_name = connection_name

    self.DEBUG = False

    if self.recv_channel_name is not None and on_message is None:
      assert self._recv_buff is not None

    super(MQTTWrapper, self).__init__(**kwargs)
    return

  def P(self, s, color=None, **kwargs):
    if color is None or (isinstance(color, str) and color[0] not in ['e', 'r']):
      color = COLORS.COMM
    comtype = self._comm_type[:7] if self._comm_type is not None else 'CUSTOM'
    self.log.P("[MQTWRP][{}] {}".format(comtype, s), color=color, **kwargs)
    return

  @property
  def nr_dropped_messages(self):
    return self.__nr_dropped_messages

  def D(self, s, t=False):
    _r = -1
    if self.DEBUG:
      if self.show_prefixes:
        msg = "[DEBUG] {}: {}".format(self.__name__, s)
      else:
        if self.prefix_log is None:
          msg = "[D] {}".format(s)
        else:
          msg = "[D]{} {}".format(self.prefix_log, s)
        # endif
      # endif
      _r = self.log.P(msg, show_time=t, color='yellow')
    # endif
    return _r

  @property
  def send_channel_name(self):
    return self._send_channel_name

  @property
  def recv_channel_name(self):
    return self._recv_channel_name

  @send_channel_name.setter
  def send_channel_name(self, x):
    if isinstance(x, tuple):
      self._send_channel_name, self._send_to = x
    else:
      self._send_channel_name = x
    return

  @recv_channel_name.setter
  def recv_channel_name(self, x):
    self._recv_channel_name = x
    return

  @property
  def cfg_eeid(self):
    return self._config.get(COMMS.EE_ID, self._config.get(COMMS.SB_ID, None))

  @property
  def cfg_user(self):
    return self._config[COMMS.USER]

  @property
  def cfg_pass(self):
    return self._config[COMMS.PASS]

  @property
  def cfg_host(self):
    return self._config[COMMS.HOST]

  @property
  def cfg_port(self):
    return self._config[COMMS.PORT]

  @property
  def cfg_qos(self):
    return self._config[COMMS.QOS]

  @property
  def recv_channel_def(self):
    if self.recv_channel_name is None:
      return

    cfg = self._config[self.recv_channel_name].copy()
    topic = cfg[COMMS.TOPIC]
    if "{}" in topic:
      topic = topic.format(self.cfg_eeid)

    cfg[COMMS.TOPIC] = topic
    return cfg

  @property
  def send_channel_def(self):
    if self.send_channel_name is None:
      return

    cfg = self._config[self.send_channel_name].copy()
    topic = cfg[COMMS.TOPIC]
    if self._send_to is not None and "{}" in topic:
      topic = topic.format(self._send_to)

    assert "{}" not in topic

    cfg[COMMS.TOPIC] = topic
    return cfg

  @property
  def connection(self):
    return self._mqttc

  def _callback_on_connect(self, client, userdata, flags, rc):
    self.connected = False
    if rc == 0:
      self.connected = True
      self.P("Conn ok clntid '{}' with code: {}".format(str(self._mqttc._client_id), rc), color='g')
    return

  def _callback_on_disconnect(self, client, userdata, rc):
    """
    Tricky callback

    we can piggy-back ride the client with flags:
      client.connected_flag = False 
      client.disconnect_flag = True
    """
    if rc == 0:
      self.P('Gracefull disconn (code={})'.format(rc), color='m')
    else:
      self.P("Unexpected disconn for client id '{}': '{}' (code={})".format(
        self._mqttc._client_id, mqtt.error_string(rc), rc), color='r'
      )
    if self._disconnected_counter > 0:
      self.P('  Multiple conn loss history: {} disconnects so far\n{}'.format(
        self._disconnected_counter, '\n'.join([f"{x1}: {x2}" for x1, x2 in self._disconnected_log])), color='r')
    self.connected = False
    self.disconnected = True
    self._disconnected_log.append((self.log.time_to_str(), mqtt.error_string(rc)))
    self._disconnected_counter += 1
    # we need to stop the loop otherwise the client thread will keep working
    # so we call release->loop_stop
    self.release()
    return

  def _callback_on_publish(self, client, userdata, mid):
    return

  def _callback_on_message(self, client, userdata, message):
    if self._custom_on_message is not None:
      self._custom_on_message(client, userdata, message)
    else:
      try:
        msg = message.payload.decode('utf-8')
        self._recv_buff.append(msg)
      except:
        # DEBUG TODO: enable here a debug show of the message.payload if
        # the number of dropped messages rises
        # TODO: add also to ANY OTHER wrapper
        self.__nr_dropped_messages += 1
    # now call the "post-process" callback
    if self._post_default_on_message is not None:
      self._post_default_on_message()
    return

  def get_connection_issues(self):
    return {x1: x2 for x1, x2 in self._disconnected_log}

  def server_connect(self, max_retries=5):
    nr_retry = 1
    has_connection = False
    exception = None
    sleep_iter = None
    comtype = self._comm_type[:7] if self._comm_type is not None else 'CUSTOM'

    while nr_retry <= max_retries:
      try:
        client_uid = self.log.get_unique_id()
        self._mqttc = mqtt.Client(
          client_id=self._connection_name + '_' + comtype + '_' + client_uid,
          clean_session=True
        )

        self._mqttc.username_pw_set(
          username=self.cfg_user,
          password=self.cfg_pass
        )

        self._mqttc.on_connect = self._callback_on_connect
        self._mqttc.on_disconnect = self._callback_on_disconnect
        self._mqttc.on_message = self._callback_on_message
        self._mqttc.on_publish = self._callback_on_publish
        # TODO: more verbose logging including when there is no actual exception
        self._mqttc.connect(host=self.cfg_host, port=self.cfg_port)

        if self._mqttc is not None:
          self._mqttc.loop_start()  # start loop in another thread

        sleep_time = 0.01
        max_sleep = 2
        for sleep_iter in range(1, int(max_sleep / sleep_time) + 1):
          sleep(sleep_time)
          if self.connected:
            break
        # endfor

        has_connection = self.connected
      except Exception as e:
        exception = e
        if self.debug_errors:
          self.P(e, color='r')
          self.P(traceback.format_exc(), color='r')

      # end try-except

      if has_connection:
        break

      nr_retry += 1
    # endwhile

    if hasattr(self._mqttc, '_thread') and self._mqttc._thread is not None:
      self._mqttc._thread.name = self._connection_name + '_' + comtype + '_' + client_uid
      self._thread_name = self._mqttc._thread.name

    if has_connection:
      msg = "MQTT conn ok by '{}' in {:.1f}s - {}:{}".format(
        self._thread_name, sleep_iter * sleep_time, self.cfg_host, self.cfg_port
      )
      msg_type = PAYLOAD_CT.STATUS_TYPE.STATUS_NORMAL
      self._nr_full_retries = 0
      self.P(msg, color='g')
    else:
      reason = exception
      if reason is None:
        reason = " max retries in {:.1f}s".format(sleep_iter * sleep_time)
      self._nr_full_retries += 1
      msg = 'MQTT (Paho) conn to {}:{} failed after {} retr ({} trials) (reason:{})'.format(
        self.cfg_host, self.cfg_port, nr_retry, self._nr_full_retries, reason
      )
      msg_type = PAYLOAD_CT.STATUS_TYPE.STATUS_EXCEPTION
      self.P(msg, color='r')
      # now register failure
    # endif

    dct_ret = {
      'has_connection': has_connection,
      'msg': msg,
      'msg_type': msg_type
    }

    if self._mqttc is not None and not has_connection:
      self.release()

    return dct_ret

  def get_thread_name(self):
    return self._thread_name

  def subscribe(self, max_retries=5):

    if self.recv_channel_name is None:
      return

    nr_retry = 1
    has_connection = False
    exception = None
    topic = self.recv_channel_def[COMMS.TOPIC]

    while nr_retry <= max_retries:
      try:
        self._mqttc.subscribe(
          topic=topic,
          qos=self.cfg_qos
        )
        has_connection = True
      except Exception as e:
        exception = e

      if has_connection:
        break

      sleep(1)
      nr_retry += 1
    # endwhile

    if has_connection:
      msg = "MQTT (Paho) subscribed to topic '{}'".format(topic)
      msg_type = PAYLOAD_CT.STATUS_TYPE.STATUS_NORMAL
    else:
      msg = "MQTT (Paho) subscribe to '{}' FAILED after {} retries (reason:{})".format(topic, max_retries, exception)
      msg_type = PAYLOAD_CT.STATUS_TYPE.STATUS_EXCEPTION
    # endif

    dct_ret = {
      'has_connection': has_connection,
      'msg': msg,
      'msg_type': msg_type
    }

    return dct_ret

  def receive(self):
    return

  def send(self, message):
    if self._mqttc is None:
      return

    result = self._mqttc.publish(
      topic=self.send_channel_def[COMMS.TOPIC],
      payload=message,
      qos=self.cfg_qos
    )

    ####
    self.D("Sent message '{}'".format(message))
    ####

    if result.rc == mqtt.MQTT_ERR_QUEUE_SIZE:
      raise ValueError('Message is not queued due to ERR_QUEUE_SIZE')

    return

  def release(self):
    try:
      self._mqttc.disconnect()
      self._mqttc.loop_stop()  # stop the loop thread
      self.connected = False
      del self._mqttc
      self._mqttc = None
      msg = 'MQTT (Paho) connection released.'
    except Exception as e:
      msg = 'MQTT (Paho) exception while releasing connection: `{}`'.format(str(e))

    dct_ret = {'msgs': [msg]}
    return dct_ret
