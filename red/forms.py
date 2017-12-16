from django import forms


class DeviceStatus(forms.Form):
    data = forms.CharField(label='data', max_length=2000)


class PaperForm(forms.Form):
    title = forms.CharField(label='data', max_length=140)
    content = forms.CharField(label='data', max_length=2000)
