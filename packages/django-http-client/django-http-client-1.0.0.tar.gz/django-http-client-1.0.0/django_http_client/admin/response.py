__all__ = ["ResponseAdmin"]

from datetime import datetime
import os

from django.contrib import admin
from django.utils.timesince import timesince

from ..models import Response


class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        "host",
        "url",
        "status",
        "disk_relpath",
        "priority",
        "time",
        "timesince",
    ]
    readonly_fields = ["content", "headers", "request_headers"]
    search_fields = [
        "url",
    ]

    def content(self, obj):
        path = os.path.join(self.disk_relpath, "content")
        return open(path).read() if os.path.exists(path) else None

    def headers(self, obj):
        path = os.path.join(self.disk_relpath, "headers")
        return open(path).read() if os.path.exists(path) else None

    def request_headers(self, obj):
        path = os.path.join(self.disk_relpath, "request", "headers")
        return open(path).read() if os.path.exists(path) else None

    def time(self, obj):
        return datetime.fromtimestamp(obj.timestamp)

    time.short_description = "time"

    def timesince(self, obj):
        return "%s ago" % timesince(datetime.fromtimestamp(obj.timestamp))

    timesince.short_description = "timesince"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Response, ResponseAdmin)
