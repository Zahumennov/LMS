import re

from django.core.exceptions import ValidationError


def validate_email_for_prohibited_domain(value):

    if '@mail.ru' in value:
        raise ValidationError('Prohibited domain!')

    return value


def validate_phone(value):

    short_length = 13

    pattern = '(\(\d\d\d\)|\+\d\d\(\d\d\d\))\d\d\d\-\d\d\d\d'  # noqa

    if not re.match(pattern, value):
        raise ValidationError('Phone number is not correct')

    if len(value) == short_length:
        value = '+38' + value

    return value
