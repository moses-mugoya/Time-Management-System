from django.contrib import admin
from .models import Activities


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'created', 'modified', 'duration', 'date']
    list_filter = ['user', 'date']
    list_display_links = ['user']


admin.site.register(Activities, ActivityAdmin)

