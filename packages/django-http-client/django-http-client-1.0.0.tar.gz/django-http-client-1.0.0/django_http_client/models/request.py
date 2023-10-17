__all__ = ["AbstractRequest", "Request"]

import json
import os

from django.db import models

from ..utils import get_timestamp
from .mixins import HeadersMixin


class AbstractRequest(HeadersMixin, models.Model):
    host = models.CharField(max_length=255, help_text="used for load balancing")
    url = models.CharField(max_length=255)
    method = models.CharField(default="GET", max_length=255)
    proxy = models.TextField(null=True)
    data = models.TextField(null=True)
    cookies = models.TextField(null=True)
    headers = models.TextField(null=True)
    allow_redirects = models.BooleanField(default=True)
    disk_path = models.CharField(null=True, max_length=1024)
    max_redirects = models.IntegerField(null=True, default=10)
    max_retries = models.IntegerField(null=True, default=1)
    retries_count = models.IntegerField(null=True, default=0)
    verify_ssl = models.BooleanField(null=True, default=False)
    timeout = models.IntegerField(null=True)
    priority = models.IntegerField(null=True, default=0)
    created_at = models.FloatField(null=True, default=get_timestamp)
    updated_at = models.FloatField(null=True)

    class Meta:
        abstract = True

    def get_data(self):
        return json.loads(self.data) if self.data else {}

    def get_cookies(self):
        return json.loads(self.cookies) if self.cookies else {}


class Request(AbstractRequest):
    class Meta:
        db_table = "http_client_request"
