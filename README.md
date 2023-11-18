# udp2mqtt
Status: *WIP*

# Installation
+ Install and upgrade deps `pip3 install -r requirements.txt -U`
+ Install and upgrade deps `pip3 install -r requirements-test.txt -U`

# Durations testing
+ `mosquitto_pub -h broker.hivemq.com -t  /moip/udp2mqtt/durations -m '{ "durations": [60, -60, 180, -60, 380, -60] , "version": 1}'`
+ Testing with bug (CWCOM) ` mosquitto_pub -h broker.hivemq.com -t  /moip/udp2mqtt/durations -m '{ "durations": [ -347, 145, -183, 51, -160, 51, -47, 47, -51, 47, -211, 144 ]  , "version": 1}'`

+ `mosquitto_sub -h broker.hivemq.com -t  /moip/udp2mqtt/durations`

# Free accounts
- https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/
- broker.hivemq.com	1883	websocket	8000

