from django.db import models # noqa

from core.validators import validate_email_for_prohibited_domain, validate_phone


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)

    email = models.EmailField(default=64, validators=[
        validate_email_for_prohibited_domain,
    ])
    phone_number = models.CharField(null=False, default='+38(000)000-000', max_length=20,
                                    validators=[validate_phone])

    def __str__(self):
        return f'Student - {self.first_name} - {self.last_name} - {self.age} - {self.email} - ' \
               f'{self.phone_number}'
