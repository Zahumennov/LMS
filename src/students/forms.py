from django.forms import ModelForm

from students.models import Student, Teacher, Group


class StudentCreateForm(ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']


class TeacherCreateForm(ModelForm):

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'email', 'birth_date', 'phone_number']


class GroupCreateForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name']

