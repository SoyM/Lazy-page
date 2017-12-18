from django import forms


class AccountForm(forms.Form):
    username = forms.CharField(label='username', max_length=15)
    password = forms.CharField(label='password', max_length=15)


class DeviceStatus(forms.Form):
    data = forms.CharField(label='data', max_length=2000)


class PaperForm(forms.Form):
    title = forms.CharField(label='title', max_length=140)
    content = forms.CharField(label='content', max_length=2000)
