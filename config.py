# Configuration for UDP connections
SERVER_IP = "mopp_chat_server" #"127.0.0.1"  # "10.101.101.14" 
#SERVER_IP = "10.101.101.14" #"127.0.0.1"  # "" 
UDP_PORT = 7373

# Configuration for Chat Server
CLIENT_TIMEOUT = 3000
MAX_CLIENTS = 100
KEEPALIVE = 10
CHAT_WPM = 20

# MQTT configuration
MQTT_HOST = "broker.hivemq.com"
MQTT_PORT = 1883

TOPIC = "/moip/udp2mqtt/mopp"
TOPICDURATIONS = "/moip/udp2mqtt/durations"

MORSE_JSON_VERSION = 1