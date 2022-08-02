from django.core.exceptions import ValidationError


def validate_email_for_prohibited_domain(value):

    if '@mail.ru' in value:
        raise ValidationError(f'Prohibited domain!')

    return value
