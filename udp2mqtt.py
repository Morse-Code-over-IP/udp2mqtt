#!/usr/local/bin/python3

import paho.mqtt.client as paho
import logging
from mopp import * 
import config
import socket
import time
import sys

logging.basicConfig(level=logging.DEBUG, format='%(message)s', )

mopp = Mopp()

# UDP
print ("Connecting to UDP")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.connect((config.SERVER_IP, config.UDP_PORT))  # connect to the server
client_socket.send(mopp.mopp(20,'hi')) # Register chat server


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))
    sys.stdout.flush() # TODO: use logging

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    r = mopp.decode_message(msg.payload)
    print (r)
    sys.stdout.flush() # TODO: use logging

    client_socket.send(msg.payload)

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    sys.stdout.flush() # TODO: use logging
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    sys.stdout.flush() # TODO: use logging

def on_log(mqttc, obj, level, string):
    print(string)
    sys.stdout.flush() # TODO: use logging




# MQTT
print ("Connecting to MQTT")
sys.stdout.flush() # TODO: use logging
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect(config.MQTT_HOST, config.MQTT_PORT, 60)
mqttc.subscribe(config.MQTT_TOPIC, 0)
# FIXME: Listen to durations
mqttc.loop_start()

last_r = {} # keep track of duplicate messages...

# Main loop
while KeyboardInterrupt:
  time.sleep(0.2) # anti flood

  # FIXME: ADD KEEPALIVE SIGNAL

  try:
    data_bytes, addr = client_socket.recvfrom(64)
    client = addr[0] + ':' + str(addr[1])
    r = mopp.decode_message(data_bytes)
    print (r)
    sys.stdout.flush() # TODO: use logging
    
    # If message received send the duration json over mqtt
    if not "Keepalive" in r:
        b = Mopp(speed=r["Speed"])
        if not last_r == r:
            last_r = r

            # decode the mopp message to a json string containing the durations
            mydecoded = json.loads(b.return_duration_json(r["Message"]))

            mydecoded.update({ "version": config.MORSE_JSON_VERSION, })
            print (mydecoded)
            sys.stdout.flush() # TODO: use logging

            # And send mqtt
            infot = mqttc.publish(config.MQTT_TOPIC, json.dumps(mydecoded), qos=2)
            infot.wait_for_publish()
    


  except (KeyboardInterrupt, SystemExit):
    client_socket.close()
    break
    pass


