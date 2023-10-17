__all__ = [
    "AbstractRequestException",
    "RequestException",
]

import json

from django.db import models

from .mixins import RequestInfoMixin


class AbstractRequestException(RequestInfoMixin, models.Model):
    host = models.TextField()
    url = models.TextField()
    request_info = models.TextField()
    exc_type = models.TextField()
    exc_message = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        abstract = True


class RequestException(AbstractRequestException):
    class Meta:
        db_table = "http_client_request_exception"
