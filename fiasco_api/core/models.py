from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractUser):
    income = models.IntegerField(default=50000)

