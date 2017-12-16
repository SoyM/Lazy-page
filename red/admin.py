from django.contrib import admin
from .models import Paper, DeviceMiLed, Account


class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['content']
    fieldsets = [
        ('Main', {'fields': ['title', 'content']}),
        ('Date', {'fields': ['pub_date']})
    ]


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'mode', 'email')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('data', 'update_date')
    list_filter = ['update_date']


admin.site.register(Paper, PaperAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(DeviceMiLed, DeviceAdmin)
