<<<<<<< HEAD
from django import forms


class AccountForm(forms.Form):
    username = forms.CharField(label='username', max_length=15)
    password = forms.CharField(label='password', max_length=15)


class DeviceStatus(forms.Form):
    data = forms.CharField(label='data', max_length=2000)


class MachineParamsForm(forms.Form):
    temperature = forms.IntegerField()
    humidity = forms.IntegerField()
    mq = forms.IntegerField()
    ssid = forms.CharField(max_length=60)
=======
from django import forms


class AccountForm(forms.Form):
    username = forms.CharField(label='username', max_length=15)
    password = forms.CharField(label='password', max_length=15)


class DeviceStatus(forms.Form):
    data = forms.CharField(label='data', max_length=2000)


class MachineParamsForm(forms.Form):
    temperature = forms.IntegerField()
    humidity = forms.IntegerField()
    mq = forms.IntegerField()
    ssid = forms.CharField(max_length=60)
>>>>>>> e96c7f02342ad210bbbb123664d78f0ea4d7b9eb
