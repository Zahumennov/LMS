import django_filters
from django.forms import ModelForm

from groups.models import Group


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group

        fields = {
            'name': ['exact', 'icontains', 'startswith'],
        }


class GroupCreateForm(ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
