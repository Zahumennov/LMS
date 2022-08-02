from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student


@csrf_exempt
def get_students(request):
    students = Student.objects.all().order_by('-id')

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
            param_elems = param_value.split(',')
            if param_elems:
                or_filter = Q()
                for param_elem in param_elems:
                    or_filter |= Q(**{param_name: param_elem})
                students = students.filter(or_filter)
            else:
                students = students.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='students-list.html',
        context={'students': students}
    )


@csrf_exempt
def create_student(request):

    if request.method == 'POST':

        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list'))

    else:

        form = StudentCreateForm()

    return render(
        request=request,
        template_name='students-create.html',
        context={'form': form}
    )


@csrf_exempt
def update_student(request, id): # noqa

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentUpdateForm(
            data=request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list'))

    else:

        form = StudentCreateForm(instance=student)

    return render(
        request=request,
        template_name='students-update.html',
        context={'form': form}
    )
