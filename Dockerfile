FROM python:3

WORKDIR /app
RUN mkdir logs
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD requirements-test.txt .
RUN pip3 install -r requirements-test.txt
ADD *.py /app/

ENTRYPOINT [ "python3", "./udp2mqtt.py" ]
