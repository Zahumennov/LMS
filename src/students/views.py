from django.db.models import Q
from django.http import HttpRequest, HttpResponse  # noqa
from django.shortcuts import render  # noqa

from students.models import Student, Teacher
from students.utils import format_list


def get_students(request):
    students = Student.objects.all()

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

    form = """
    <form action="/students">
      <label >First name:</label><br>
      <input type="text" name="first_name" placeholder="Enter name"><br>
      
      <label >Last name:</label><br>
      <input type="text" name="last_name" placeholder="Enter last name"><br>
      
      <label >Last name:</label><br>
      <input type="number" name="age" placeholder="Enter age"><br><br>
      
      <input type="submit" value="Submit">
    </form> 
    """

    result = format_list(students)

    return HttpResponse(form + result)


def get_teachers(request):
    teachers = Teacher.objects.all()

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

    result = format_list(teachers)
    return HttpResponse(result)
