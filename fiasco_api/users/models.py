from django.contrib.auth.models import AbstractUser
from django.db import models

from colorizer.models import Colour
from core.mixins import Trackable
from tags.models import Tag

COLORS = [
    {'name': 'Black',
     'code': '#000'},
    {'name': 'Red',
     'code': '#f00'},
    {'name': 'Blue',
     'code': '#00f'},
    {'name': 'Green',
     'code': '#0f0'},
    {'name': 'White',
     'code': '#fff'}
]

TAGS = (
    {'label': 'еда'},
    {'label': 'аренда'},
    {'label': 'токсик'},
    {'label': 'одежда'},
    {'label': 'музыка'},
    {'label': 'спорт'},
    {'label': 'путешествия'},
    {'label': 'подарки'},
    {'label': 'кафе'},
    {'label': 'такси'},
    {'label': 'лекарства'},
    {'label': 'дом'},
)


class User(Trackable, AbstractUser):
    income = models.IntegerField(default=50000)

    def populate_initial_models(self):
        print(f"Populating color pallette for {self.username}...")
        for color in COLORS:
            Colour.objects.create(owner=self, **color)

        print(f"Populating tags for {self.username}...")
        for tag in TAGS:
            Tag.objects.create(owner=self, **tag)
