from django.db import models
from datetime import datetime
import time


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


class MachineParams(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    mq = models.IntegerField()
    ssid = models.CharField(max_length=60)
    update_date = models.DateTimeField()

    @classmethod
    def create(cls, data):
        data['update_date'] = datetime.now()
        temp = cls(temperature=data["temperature"], humidity=data["humidity"], mq=data["mq"], ssid=data["ssid"],
                   update_date=data["update_date"])
        temp.save()
        return temp.id


class BotMotion(models.Model):
    set_mode = models.CharField(max_length=50)
    bot_mode = models.CharField(max_length=50)
    update_date = models.DateTimeField()

    @classmethod
    def create(cls, data):
        if 'set_mode' in data:
            update_data = cls(id=1, set_mode=data['set_mode'], update_date=time.strftime("%Y-%m-%d %H:%M:%S"))
            update_data.save()
            return update_data.id
        if 'bot_mode' in data:
            print("c")
            update_data = cls(id=1, bot_mode=data['bot_mode'], update_date=datetime.now())
            update_data.save()
            return update_data.id

# class DeviceEspConfig(models.Model):
#     ssid_main = models.CharField(max_length=50)
#     pwd_main = models.CharField(max_length=50)
#     ssid_2 = models.CharField(max_length=50)
#     pwd_2 = models.CharField(max_length=50)
#     ssid_3 = models.CharField(max_length=50)
#     pwd_3 = models.CharField(max_length=50)
#     led_power = models.BooleanField()
#     led_bright = models.IntegerField()
