import random

from django.core.management.base import BaseCommand
from faker import Faker

from groups.models import Group
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Update teachers teachers fields with Faker'  # noqa

    def handle(self, *args, **kwargs):
        fake = Faker()

        teachers = Teacher.objects.all()

        for teacher in teachers:
            teacher.first_name = fake.first_name()
            teacher.last_name = fake.last_name()
            teacher.age = random.randint(15, 105)
            teacher.email = fake.ascii_free_email()
            teacher.birth_date = fake.date_between()
            teacher.phone_number = f'+38({random.randint(100, 999)})-{random.randint(100, 999)}' \
                                   f'-{random.randint(1000, 9999)}'
            teacher.group = Group.objects.get(id=f'{random.randint(1,5)}')

            teacher.save()
