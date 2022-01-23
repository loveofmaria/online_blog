from django.contrib import admin

from .models import RequestRecord


# Register your models here.
@admin.register(RequestRecord)
class RequestRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'location', 'os_info', 'browser', 'access_time')
