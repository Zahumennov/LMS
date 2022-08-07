from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all().order_by('-id')

    form = TeacherFilter(
        data=request.GET,
        queryset=teachers
    )

    return render(
        request=request,
        template_name='teachers-list.html',
        context={'form': form}
    )


def create_teacher(request):
    if request.method == 'POST':

        form = TeacherCreateForm(data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    else:

        form = TeacherCreateForm()

    return render(
        request=request,
        template_name='teachers-create.html',
        context={'form': form}
    )


def update_teacher(request, id):  # noqa

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':

        form = TeacherCreateForm(
            data=request.POST,
            instance=teacher
        )

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    else:

        form = TeacherCreateForm(instance=teacher)

    return render(
        request=request,
        template_name='teachers-update.html',
        context={'form': form}
    )


def delete_teacher(request, id):  # noqa

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':

        teacher.delete()

        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers-delete.html',
        context={'teacher': teacher}
    )
