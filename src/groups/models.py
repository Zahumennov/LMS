from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    headman = models.OneToOneField(
        to='students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )
    course = models.OneToOneField(
        to='courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        related_name='course_group'
    )

    def __str__(self):
        return f'Group - {self.name} '
