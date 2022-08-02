from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student


class StudentBaseForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

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
