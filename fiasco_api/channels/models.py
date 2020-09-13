from django.db import models
from django.conf import settings
from core.mixins import Trackable


class Channel(Trackable, models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
