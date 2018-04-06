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
        temperature = data["temperature"]
        temp = cls(temperature=temperature, humidity=data["humidity"], mq=data["mq"], ssid=data["ssid"],
                   update_date=datetime.now())
        temp.save()
        KalmanFilter.kalman_filter('temperature', temperature)
        return temp.id


class KalmanFilter(models.Model):
    type = models.CharField(max_length=60)
    value_filtered = models.FloatField()
    covariance = models.FloatField()
    update_date = models.DateTimeField()

    @classmethod
    def create(cls, data):
        temp = cls(type=data['type'], value_filtered=data['value_filtered'], covariance=data['covariance'],
                   update_date=data['update_date'])
        temp.save()
        return temp.id

    @staticmethod
    def kalman_filter(value_type, value):
        q = 1e-5
        r = 0.1 ** 2
        result = KalmanFilter.objects.filter(type=value_type).last()
        value_filter_last = result.value_filtered
        p = result.covariance
        print(value_filter_last)
        # time update
        x_hatminus = value_filter_last  # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
        p_minus = p + q  # P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1

        # measurement update
        k = p_minus / (p_minus + r)  # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
        value_fileted = x_hatminus + k * (float(value) - x_hatminus)  # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
        p_next = (1 - k) * p_minus  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1
        KalmanFilter.create(data={
            'type': value_type,
            'value_filtered': value_fileted,
            'covariance': p_next,
            'update_date': datetime.now()
        })
        return value_fileted, p_next


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
