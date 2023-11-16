# udp2mqtt

# Installation
+ Install and upgrade deps `pip3 install -r requirements.txt -U`
+ Install and upgrade deps `pip3 install -r requirements-test.txt -U`

# Durations testing
mosquitto_pub -h broker.hivemq.com -t  /moip/udp2mqtt/durations -m '{ "durations": [60, -60, 180, -60, 180, -60] }'


# Free accounts
# https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/
# broker.hivemq.com	1883	websocket	8000

