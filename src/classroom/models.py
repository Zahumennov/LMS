import random

from django.db import models

from groups.models import Group


class Classroom(models.Model):
    number = models.IntegerField(null=False, default=random.randint(100, 999))
    class_groups = models.ManyToManyField(
        to=Group,
        related_name='group_classes'
    )
