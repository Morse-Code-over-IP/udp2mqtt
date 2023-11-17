FROM python:3

WORKDIR /app
RUN mkdir logs
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD requirements-test.txt .
RUN pip3 install -r requirements-test.txt
ADD *.py /app/

# Configuration for UDP connections
ENV SERVER_IP "mopp_chat_server"
ENV UDP_PORT "7373"

# Configuration for Chat Server
ENV CLIENT_TIMEOUT "300"
ENV MAX_CLIENTS "100"
ENV KEEPALIVE "10"
ENV CHAT_WPM "20"

# MQTT configuration
ENV MQTT_HOST "broker.hivemq.com"
ENV MQTT_PORT "1883"
ENV MQTT_TOPIC "/moip/udp2mqtt/durations"


ENTRYPOINT [ "python3", "./udp2mqtt.py" ]
