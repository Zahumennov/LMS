from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse

from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    students = Student.objects.all().order_by('-id')

    form = StudentFilter(
        data=request.GET,
        queryset=students
    )

    return render(
        request=request,
        template_name='students-list.html',
        context={
            'form': form,
        }
    )


def create_student(request):

    if request.method == 'POST':

        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

    else:

        form = StudentCreateForm()

    return render(
        request=request,
        template_name='students-create.html',
        context={'form': form}
    )


def update_student(request, id): # noqa

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentUpdateForm(
            data=request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

    else:

        form = StudentCreateForm(instance=student)

    return render(
        request=request,
        template_name='students-update.html',
        context={'form': form}
    )


def delete_student(request, id): # noqa

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students-delete.html',
        context={'student': student}
    )
