import random
from datetime import datetime

from django.db import models

from faker import Faker

from core.validators import validate_email_for_prohibited_domain, validate_phone


class Student(models.Model):

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)

    email = models.EmailField(default=64, validators=[
        validate_email_for_prohibited_domain,
    ])
    phone_number = models.CharField(null=False, max_length=20, validators=[
        validate_phone
    ])

    enroll_date = models.DateField(default=datetime.today)
    graduate_date = models.DateField(default=datetime.today)

    def __str__(self):
        return f'Student - {self.first_name} - {self.last_name} - {self.age} - {self.email} - ' \
               f'{self.phone_number} - {self.enroll_date} - {self.graduate_date}'

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
