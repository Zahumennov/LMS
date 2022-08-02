from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f'Group - {self.name}'
