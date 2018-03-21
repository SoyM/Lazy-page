from django.contrib import admin
from .models import DeviceMiLed, MachineParams


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('data', 'update_date')
    list_filter = ['update_date']


class MachineParamsAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'mq', 'ssid', 'update_date')
    list_filter = ['update_date']


admin.site.register(DeviceMiLed, DeviceAdmin)
admin.site.register(MachineParams, MachineParamsAdmin)
