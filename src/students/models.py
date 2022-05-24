from django.db import models


class Students(models.Model):

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)


class Teacher(models.Model):

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)


class Group(models.Model):

    name = models.CharField(max_length=64, null=False)



