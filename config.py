import os

# Configuration for UDP connections
SERVER_IP = os.environ.get('SERVER_IP', "mopp_chat_server")
UDP_PORT = int(os.environ.get('UDP_PORT', "7373"))

# Configuration for Chat Server
CLIENT_TIMEOUT = int(os.environ.get('CLIENT_TIMEOUT', "300"))
MAX_CLIENTS = int(os.environ.get('MAX_CLIENTS', "100"))
KEEPALIVE = int(os.environ.get('KEEPALIVE', "10"))
CHAT_WPM = int(os.environ.get('CHAT_WPM', "20"))

# MQTT configuration
MQTT_HOST = os.environ.get('MQTT_HOST', "broker.hivemq.com")
MQTT_PORT = int(os.environ.get('MQTT_PORT', "1883"))
MQTT_TOPIC = os.environ.get('MQTT_TOPIC', "/moip/udp2mqtt/durations")

# Internal configuration with code dependencies
MORSE_JSON_VERSION = 1
MQTT_CLIENT_UNIQUE_IDENTIFIER = "123123123"