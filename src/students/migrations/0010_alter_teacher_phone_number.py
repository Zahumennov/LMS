# Generated by Django 4.0.4 on 2022-07-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_student_graduate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default='+38(063)000-1111', max_length=16),
        ),
    ]