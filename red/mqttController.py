import time
import paho.mqtt.client as mqtt

HOST = "m13.cloudmqtt.com"
PORT = 15873


class MqttController:
    def client_loop(self):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        client = mqtt.Client(client_id)
        client.username_pw_set("lytlmnde", "3mtD81MmaVqW")
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(HOST, PORT)
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("test")
        client.subscribe("admin")
        client.subscribe("servoAin")

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))
