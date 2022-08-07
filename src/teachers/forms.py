import django_filters
from django.forms import ModelForm

from teachers.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher

        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }


class TeacherCreateForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
