# Generated by Django 4.0.4 on 2022-08-16 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teachers',
            new_name='corse_teachers',
        ),
    ]
