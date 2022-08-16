import random

from faker import Faker
from django.core.management.base import BaseCommand, CommandError

from students.models import Student


class Command(BaseCommand):
    help = 'Generates specified amount of students' # noqa

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The amount of added students')

    def handle(self, *args, **kwargs):
        try:
            faker = Faker()
            count = kwargs['count']
            for _ in range(count):
                student = Student()
                student.first_name = faker.first_name()
                student.last_name = faker.last_name()
                student.age = random.randint(30, 80)
                student.email = faker.email()
                student.phone_number = f'+38({random.randint(100, 999)})' \
                                       f'{random.randint(100, 999)}-{random.randint(1000, 9999)}'
                student.enroll_date = faker.date()
                student.graduate_date = faker.date()
                student.group_id = random.randint(1, 5)
                student.save()
        except CommandError as ce:
            raise CommandError(f'{ce}')
        self.stdout.write(f'Successfully generated {count} students')
