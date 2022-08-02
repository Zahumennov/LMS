from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect  # noqa
from django.shortcuts import render  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, TeacherCreateForm, GroupCreateForm, StudentUpdateForm
from students.models import Student, Teacher, Group
from students.utils import format_list


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

    result = format_list(teachers, '/teachers/update/')
    return HttpResponse(result)


@csrf_exempt
def create_teacher(request):

    if request.method == 'POST':

        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/teachers/')

    if request.method == 'GET':
        form = TeacherCreateForm()

    html_template = """
    <form method='post'>
      {}

      <input type="submit" value="Create">
    </form>
    """

    result = html_template.format(form.as_p())

    return HttpResponse(result)


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

            return HttpResponseRedirect('/teachers/')

    elif request.method == 'GET':

        form = TeacherCreateForm(instance=teacher)

    html_template = """
    <form method='post'>
      {}

      <input type="submit" value="Update">
    </form>
    """

    result = html_template.format(form.as_p())

    return HttpResponse(result)


def get_groups(request):
    groups = Group.objects.all().order_by('-id')

    params = [
        'name'
    ]

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            groups = groups.filter(**{param_name: param_value})

    result = format_list(groups, '/groups/update/')
    return HttpResponse(result)


@csrf_exempt
def create_group(request):

    if request.method == 'POST':

        form = GroupCreateForm(request.POST)

        form.save()

        return HttpResponseRedirect('/groups/')

    if request.method == 'GET':

        form = GroupCreateForm()

    html_template = """
    <form method='post'>
      {}

      <input type="submit" value="Create">
    </form>
    """

    result = html_template.format(form)

    return HttpResponse(result)


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

            return HttpResponseRedirect('/groups/')

    if request.method == 'GET':
        form = GroupCreateForm(instance=group)

    html_template = """
    <form method='post'>
      {}

      <input type="submit" value="Update">
    </form>
    """

    result = html_template.format(form)

    return HttpResponse(result)
