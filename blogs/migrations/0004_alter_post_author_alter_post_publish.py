# Generated by Django 4.2.4 on 2023-08-16 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_post_author_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 2, 4, 50, 808342)),
        ),
    ]