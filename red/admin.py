from django.contrib import admin
from .models import Paper


class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['content']
    fieldsets = [
        ('Main', {'fields': ['title', 'content']}),
        ('Date', {'fields': ['pub_date']})
    ]


admin.site.register(Paper, PaperAdmin)
