from django.db import models
from django.conf import settings
from core.mixins import Trackable


class Colour(Trackable, models.Model):
    name = models.TextField()
    code = models.CharField(max_length=7)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('name', 'owner'), name='unique_name_for_user'),
        ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
