# Generated by Django 5.0.4 on 2024-06-19 10:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1995), django.core.validators.MaxValueValidator(2025)]),
        ),
    ]