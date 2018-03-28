#!/usr/bin/env python
# -*- coding: utf-8 -*
# foolbot @ Python
# Functions: foolbot controller
# Created By SoyM on 2018-03-28,Version 0.1

import threading
from red.mqttController import MqttController
import os


if __name__ == "__main__":
    mqtt = MqttController()
    t1 = threading.Thread(target=mqtt.client_loop)
    t1.setDaemon(True)
    t1.start()
    os.system("python manage.py runserver 0.0.0.0:8000")

