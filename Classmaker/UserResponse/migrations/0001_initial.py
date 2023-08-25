# Generated by Django 4.2.3 on 2023-08-24 07:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestingSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserINFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ')),
                ('ms_name', models.CharField(choices=[('M5', 'Main-Season-5'), ('M6', 'Main-Season-6'), ('M7', 'Main-Season-7'), ('M8', 'Main-Season-8'), ('M9', 'Main-Season-9')], max_length=2)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserTimePassed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_time', models.DateTimeField(auto_now_add=True)),
                ('ended_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserResponseModelTrueFalseOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_based', models.BooleanField()),
                ('question_based', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses_truefalse', to='TestingSystem.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_truefalse', to='UserResponse.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponseModelMultiOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_based', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses_multiple', to='TestingSystem.option')),
                ('question_based', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses_multiple', to='TestingSystem.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_multiple', to='UserResponse.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponseModelFreeTextOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_based', models.TextField(max_length=300)),
                ('question_based', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses_freetext', to='TestingSystem.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_freetext', to='UserResponse.userinfo')),
            ],
        ),
    ]
