#!/usr/local/bin/python3
# Simple transmitter

import paho.mqtt.client as paho
import logging
from mopp import * 
import config
import socket
import logging
import time
from mopp import * 
from beep import *
import config

logging.basicConfig(level=logging.DEBUG, format='%(message)s', )

mopp = Mopp()



def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    r = mopp.decode_message(msg.payload)
    print (r)

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)


# MQTT
print ("Connecting to MQTT")
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect(config.MQTT_HOST, config.MQTT_PORT, 60)
mqttc.loop_start()


# UDP
print ("Connecting to UDP")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.connect((config.SERVER_IP, config.UDP_PORT))  # connect to the server
client_socket.send(mopp.mopp(20,'hi')) # Register chat server

last_r = {} # keep track of duplicate messages...

# Main loop
while KeyboardInterrupt:
  time.sleep(0.2)						# anti flood
  try:
    data_bytes, addr = client_socket.recvfrom(64)
    client = addr[0] + ':' + str(addr[1])
    r = mopp.decode_message(data_bytes)
    print (r)
    
    # Beep if message received
    if not "Keepalive" in r:
        #b = Beep(speed=r["Speed"])
        if not last_r == r:
            #b.beep_message(r["Message"])
            last_r = r

            # And send mqtt
            infot = mqttc.publish("m32_test", data_bytes, qos=2)
            infot.wait_for_publish()
    


  except (KeyboardInterrupt, SystemExit):
    client_socket.close()
    break
    pass


