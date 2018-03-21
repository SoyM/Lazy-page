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
