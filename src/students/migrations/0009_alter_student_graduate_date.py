# Generated by Django 4.0.4 on 2022-07-30 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_student_graduate_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduate_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]