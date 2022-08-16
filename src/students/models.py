import random
from datetime import datetime

from django.db import models

from faker import Faker

from core.models import Person
from groups.models import Group


class Student(Person):
    enroll_date = models.DateField(default=datetime.today)
    graduate_date = models.DateField(default=datetime.today)

    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.SET_NULL,
        related_name='students',
    )

    def __str__(self):
        return f'Student - {self.first_name} - {self.last_name} - {self.age} - {self.email} - ' \
               f'{self.phone_number} - {self.enroll_date} - {self.graduate_date} - ' \
               f'{self.group}'

    @classmethod
    def generate_students(cls, count):
        faker = Faker()

        for _ in range(count):
            student = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(15, 105)
            )

            student.save()
