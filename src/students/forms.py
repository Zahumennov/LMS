import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student, Teacher, Group


class StudentBaseForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def clean_phone_number(self):

        short_length = 13

        phone_number = self.cleaned_data['phone_number']
        pattern = '(\(\d\d\d\)|\+\d\d\(\d\d\d\))\d\d\d\-\d\d\d\d' # noqa

        if not re.match(pattern, phone_number):
            raise ValidationError('Phone number is not correct')

        if len(phone_number) == short_length:
            phone_number = '+38' + phone_number

        return phone_number

    def clean_email(self):

        email = self.cleaned_data['email']

        emails = Student.objects.filter(email=email).exclude(id=self.instance.id).exists()

        if emails:
            raise ValidationError(f'{email} already exists.')

        return email

    def clean(self):
        result = super().clean()
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']

        if enroll_date > graduate_date:
            raise ValidationError("Enroll date couldn\'t be after graduate date")

        return result


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):

    class Meta(StudentBaseForm.Meta):
        exclude = ['age']


class TeacherCreateForm(ModelForm):

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'email', 'birth_date', 'phone_number']


class GroupCreateForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name']
