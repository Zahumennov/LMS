# Generated by Django 4.0.4 on 2022-08-02 09:41

import core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=84)),
                ('age', models.IntegerField(default=42)),
                ('email', models.EmailField(default='example@gmail.com', max_length=254)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(default='+38(063)000-1111', max_length=16, validators=[core.validators.validate_phone])),
            ],
        ),
    ]
