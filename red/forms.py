from django import forms


class DeviceStatus(forms.Form):
    data = forms.CharField(label='data', max_length=2000)
