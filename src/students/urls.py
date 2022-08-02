"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from students.views import get_students, get_teachers, create_student, create_teacher, get_groups, \
    create_group, update_student, update_teacher, update_group

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include('debug_toolbar.urls')),

    path('students/', get_students),
    path('students/create', create_student),
    path('students/update/<int:id>', update_student),
    path('teachers/', get_teachers),
    path('teachers/create', create_teacher),
    path('teachers/update/<int:id>', update_teacher),
    path('groups/', get_groups),
    path('groups/create', create_group),
    path('groups/update/<int:id>', update_group),
]