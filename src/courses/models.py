from django.db import models

from teachers.models import Teacher


class Course(models.Model):
    code = models.CharField(max_length=5, null=False, default='UKR00')
    name = models.CharField(max_length=30, null=False, default='Course')
    duration = models.SmallIntegerField(null=False, default=4)
    course_teachers = models.ManyToManyField(
        to=Teacher,
        related_name='teacher_courses'
    )
