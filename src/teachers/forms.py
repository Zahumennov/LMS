from django.forms import ModelForm

from teachers.models import Teacher


class TeacherCreateForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
