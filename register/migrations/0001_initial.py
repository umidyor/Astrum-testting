# Generated by Django 4.2.4 on 2023-08-11 04:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regsiter_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(5)])),
            ],
        ),
    ]
