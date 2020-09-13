from django.db import models
from django.conf import settings

from core.mixins import Trackable


class Tag(Trackable, models.Model):
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=('label', 'owner'), name='unique_tag_for_user'),
    #     ]

    label = models.CharField(max_length=255, unique=True)
    display_colour = models.ForeignKey('colorizer.Colour', on_delete=models.SET_NULL, null=True, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
