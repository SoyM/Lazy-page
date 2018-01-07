from django.contrib import admin
from .models import DeviceMiLed


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('data', 'update_date')
    list_filter = ['update_date']


admin.site.register(DeviceMiLed, DeviceAdmin)
