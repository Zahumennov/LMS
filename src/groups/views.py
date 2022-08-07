from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm, GroupFilter
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all().order_by('-id')

    form = GroupFilter(
        data=request.GET,
        queryset=groups
    )

    return render(
        request=request,
        template_name='groups-list.html',
        context={'form': form}
    )


def create_group(request):

    if request.method == 'POST':

        form = GroupCreateForm(request.POST)

        form.save()

        return HttpResponseRedirect(reverse('groups:list'))

    else:

        form = GroupCreateForm()

    return render(
        request=request,
        template_name='groups-create.html',
        context={'form': form}
    )


def update_group(request, id): # noqa

    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':

        form = GroupCreateForm(
            data=request.POST,
            instance=group
        )

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    else:
        form = GroupCreateForm(instance=group)

    return render(
        request=request,
        template_name='groups-update.html',
        context={
            'form': form,
            'group': group
        }
    )


def delete_group(request, id): # noqa

    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':

        group.delete()

        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups-delete.html',
        context={'group': group}
    )
