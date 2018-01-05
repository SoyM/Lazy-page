from django.db import models
from datetime import datetime
import base64


class Paper(models.Model):
    title = models.CharField(max_length=140)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField()

    @classmethod
    def edit(cls, pk, title, content):
        if cls(pk=pk, title=title, pub_date=datetime.now(), content=base64.b64encode(content)).save():
            return True

    def __str__(self):
        return str(self.id)


class DeviceMiLed(models.Model):
    data = models.CharField(max_length=2000)
    update_date = models.DateTimeField()

    @classmethod
    def create(cls, data):
        temp = cls(data=data, update_date=datetime.now())
        temp.save()
        return temp.id

    def __str__(self):
        return str(self.id)


class DeviceEspStatus(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    mq = models.IntegerField()
    ssid = models.CharField(max_length=60)


class DeviceEspConfig(models.Model):
    ssid_main = models.CharField(max_length=50)
    pwd_main = models.CharField(max_length=50)
    ssid_2 = models.CharField(max_length=50)
    pwd_2 = models.CharField(max_length=50)
    ssid_3 = models.CharField(max_length=50)
    pwd_3 = models.CharField(max_length=50)
    led_power = models.BooleanField()
    led_bright = models.IntegerField()
