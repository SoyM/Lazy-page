from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=140)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class DeviceMiLed(models.Model):
    data = models.CharField(max_length=2000)
    update_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
