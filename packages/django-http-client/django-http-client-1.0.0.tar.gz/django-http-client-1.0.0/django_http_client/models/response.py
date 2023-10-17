__all__ = [
    "AbstractResponse",
    "Response",
]

import json
import os

import shutil

from django.db import models

from ..utils import get_headers, get_timestamp
from .mixins import HeadersMixin, RequestInfoMixin


class AbstractResponse(HeadersMixin, RequestInfoMixin, models.Model):
    url = models.CharField(max_length=255)
    status = models.IntegerField()
    headers = models.TextField(null=True)
    request_info = models.TextField(null=True)
    disk_path = models.CharField(null=True, max_length=1024)
    timestamp = models.FloatField(default=get_timestamp)

    class Meta:
        abstract = True

    def get_content(self):
        disk_path_list = [
            self.disk_path,
            os.path.join(str(self.disk_path), "content"),
        ]
        for disk_path in disk_path_list:
            if os.path.exists(disk_path):
                return open(disk_path).read()

    def get_content_data(self):
        content = self.get_content()
        if content:
            return json.loads(content)

    def delete_disk_path(self):
        if os.path.exists(self.disk_path):
            if os.path.isfile(self.disk_path):
                os.unlink(self.disk_path)
            else:
                shutil.rmtree(self.disk_path)


class Response(AbstractResponse):
    class Meta:
        db_table = "http_client_response"
        ordering = ("-timestamp",)
