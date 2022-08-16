from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from courses.forms import CourseBaseForm
from courses.models import Course


def get_courses(request):

    courses = Course.objects.all()

    return render(
        request=request,
        template_name='courses-list.html',
        context={
            'courses': courses
        }
    )


def create_course(request):

    if request.method == 'POST':

        form = CourseBaseForm(request.POST)

        form.save()

        return HttpResponseRedirect(reverse('courses:list'))

    else:

        form = CourseBaseForm()

    return render(
        request=request,
        template_name='courses-create.html',
        context={
            'form': form
        }
    )


def update_course(request, id):

    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':

        form = CourseBaseForm(
            data=request.POST,
            instance=course
        )

        form.save()

        return HttpResponseRedirect(reverse('courses:list'))

    else:

        form = CourseBaseForm(instance=course)

    return render(
        request=request,
        template_name='courses-update.html',
        context={
            'form': form,
        }
    )


def delete_course(request, id):

    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':

        course.delete()

        return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses-delete.html',
        context={'course': course}
    )
