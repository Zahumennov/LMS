import random

from django.db import models
from django.utils import timezone
from faker import Faker

from core.models import Person
from groups.models import Group


class Teacher(Person):
    birth_date = models.DateField(null=False, default=timezone.now)
    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.CASCADE,
        related_name='teacher'
    )

    def __str__(self):
        return f'Teacher - {self.first_name} - {self.last_name} - {self.age} - {self.email}' \
               f' - {self.birth_date} - {self.phone_number} - {self.group}'

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()

        for _ in range(count):
            teacher = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(30, 80),
                email=faker.email(),
                phone_number=f'+38({random.randint(100, 999)}){random.randint(100, 999)}-'
                             f'{random.randint(1000, 9999)}',
                birth_date=faker.date(),
            )

            teacher.save()
