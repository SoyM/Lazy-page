# Generated by Django 2.0 on 2017-12-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0004_auto_20171215_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=15)),
                ('mode', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]