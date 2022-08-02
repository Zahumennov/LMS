from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm
from teachers.models import Teacher


@csrf_exempt
def get_teachers(request):

    teachers = Teacher.objects.all().order_by('-id')

    params = [
        'first_name',
        'first_name__startswith',
        'first_name__endswith',
        'last_name',
        'last_name__startswith',
        'last_name__endswith',
        'age',
        'age__gt'
    ]

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='teachers-list.html',
        context={'teachers': teachers}
    )


@csrf_exempt
def create_teacher(request):

    if request.method == 'POST':

        form = TeacherCreateForm(data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teacher_list'))

    else:

        form = TeacherCreateForm()

    return render(
        request=request,
        template_name='teachers-create.html',
        context={'form': form}
    )


@csrf_exempt
def update_teacher(request, id): # noqa

    teacher = Teacher.objects.get(id=id)

    if request.method == 'POST':

        form = TeacherCreateForm(
            data=request.POST,
            instance=teacher
        )

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teacher_list'))

    else:

        form = TeacherCreateForm(instance=teacher)

    return render(
        request=request,
        template_name='teachers-update.html',
        context={'form': form}
    )
