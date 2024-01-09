# Generated by Django 4.2.4 on 2024-01-03 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0003_alter_responsemodel_response_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsemodel',
            name='response_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]