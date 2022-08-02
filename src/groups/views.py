from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Group


@csrf_exempt
def get_groups(request):
    groups = Group.objects.all().order_by('-id')

    params = [
        'name'
    ]

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            groups = groups.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='groups-list.html',
        context={'groups': groups}
    )


@csrf_exempt
def create_group(request):

    if request.method == 'POST':

        form = GroupCreateForm(request.POST)

        form.save()

        return HttpResponseRedirect(reverse('group_list'))

    else:

        form = GroupCreateForm()

    return render(
        request=request,
        template_name='groups-create.html',
        context={'form': form}
    )


@csrf_exempt
def update_group(request, id): # noqa

    group = Group.objects.get(id=id)

    if request.method == 'POST':

        form = GroupCreateForm(
            data=request.POST,
            instance=group
        )

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('group_list'))

    else:
        form = GroupCreateForm(instance=group)

    return render(
        request=request,
        template_name='groups-update.html',
        context={'form': form}
    )
