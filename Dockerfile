FROM python:3
RUN pip3 install --no-cache-dir --upgrade pip \
&& pip3 install -r --no-cache-dir requirements.txt

WORKDIR /app

COPY . .


CMD [ "python", "./mqtt_bridge.py" ]