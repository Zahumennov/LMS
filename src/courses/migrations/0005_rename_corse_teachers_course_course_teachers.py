# Generated by Django 4.0.4 on 2022-08-16 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_teachers_course_corse_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='corse_teachers',
            new_name='course_teachers',
        ),
    ]