# Generated by Django 2.0 on 2017-12-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0002_devicemiled'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceEspConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssid_main', models.CharField(max_length=50)),
                ('pwd_main', models.CharField(max_length=50)),
                ('ssid_2', models.CharField(max_length=50)),
                ('pwd_2', models.CharField(max_length=50)),
                ('ssid_3', models.CharField(max_length=50)),
                ('pwd_3', models.CharField(max_length=50)),
                ('led_power', models.BooleanField()),
                ('led_bright', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceEspStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(max_length=3)),
                ('humidity', models.IntegerField(max_length=3)),
                ('mq', models.IntegerField(max_length=3)),
                ('ssid', models.CharField(max_length=60)),
            ],
        ),
    ]
