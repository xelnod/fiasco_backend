from django.db import models
from django.conf import settings

from core.mixins import Trackable


class Cat(Trackable, models.Model):
    name = models.CharField(max_length=255)
    display_colour = models.ForeignKey('colorizer.Colour', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(default='', blank=True)
    tags = models.ManyToManyField('tags.Tag', blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Kit(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField('tags.Tag')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
