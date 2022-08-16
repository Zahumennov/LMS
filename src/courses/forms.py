from django.forms import ModelForm

from courses.models import Course


class CourseBaseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
