import time
import paho.mqtt.client as mqtt
import json
# import middleCh
import requests

HOST = "m13.cloudmqtt.com"
PORT = 15873
USER = "lytlmnde"
PASSWORD = "3mtD81MmaVqW"


class MqttController:
    def __init__(self):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.client = mqtt.Client(client_id)

    def client_loop(self):
        self.client.username_pw_set(USER, PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(HOST, PORT)
        self.client.loop_forever()

    @classmethod
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("test")
        client.subscribe("admin")
        client.subscribe("servoAin")
        client.subscribe("set_mode")
        client.subscribe("bot_mode")
        client.publish("test", json.dumps({"user": USER, "say": "Hello,anyone!"}))

    @classmethod
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))
        if msg.topic == "bot_mode":
            data = json.loads(msg.payload.decode("utf-8"))
            bot_mode = data['bot_mode']
            if bot_mode in ["up", "down", "left", "right", "auto", "wave"]:
                r = requests.post('http://127.0.0.1:8000/update_bot_motion/', json={"bot_mode": bot_mode})
                print(r.text)

    def send_message(self, topic, message):
        self.client.publish(topic, json.dumps(message))
