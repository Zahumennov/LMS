import random

from django.db import models
from django.utils import timezone

from faker import Faker

from core.validators import validate_phone


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)
    email = models.EmailField(null=False, default='example@gmail.com')
    birth_date = models.DateField(null=False, default=timezone.now)
    phone_number = models.CharField(null=False, max_length=16, default='+38(063)000-1111',
                                    validators=[
                                        validate_phone
                                    ])

    def __str__(self):
        return f'Teacher - {self.first_name} - {self.last_name} - {self.age} - {self.email}' \
               f' - {self.birth_date} - {self.phone_number}'

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()

        for _ in range(count):
            teacher = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(30, 80)
            )

            teacher.save()
