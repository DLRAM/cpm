# Generated by Django 2.2.4 on 2020-04-24 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0015_auto_20200416_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyinfo',
            name='contact',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)]),
        ),
    ]
