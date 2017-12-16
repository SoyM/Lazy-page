from django.db import models
from datetime import datetime


class Paper(models.Model):
    title = models.CharField(max_length=140)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField()

    @classmethod
    def create(cls, title, content):
        temp = cls(title=title, content=content)
        temp.save()
        return temp.id

    def __str__(self):
        return str(self.id)


class Account(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    mode = models.IntegerField()
    email = models.EmailField()


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
