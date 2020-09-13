from django.db import models


class Trackable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # created_by = models.ForeignKey(User, related_name='created_%(class)s')
    # updated_by = models.ForeignKey(User, related_name='updated_%(class)s')
    class Meta:
        abstract = True
