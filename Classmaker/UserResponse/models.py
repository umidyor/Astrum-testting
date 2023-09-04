from django.db import models
from TestingSystem.models import Question, Option, TrueFalse, FreeText
from phonenumber_field.modelfields import PhoneNumberField# Create your models here.
from django.db import models


class UserINFO(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    number = PhoneNumberField(region="UZ")
    MS = [
        ("M5", "Main-Season-5"),
        ("M6", "Main-Season-6"),
        ("M7", "Main-Season-7"),
        ("M8", "Main-Season-8"),
        ("M9", "Main-Season-9"),
    ]
    ms_name = models.CharField(max_length=2, choices=MS)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.ms_name}'


class UserResponseModelMultiOption(models.Model):
    user = models.ForeignKey(UserINFO, on_delete=models.CASCADE, related_name='user_multiple')
    question_based = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses_multiple')
    answer_based = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='responses_multiple')


class UserResponseModelTrueFalseOption(models.Model):
    user = models.ForeignKey(UserINFO, on_delete=models.CASCADE, related_name='user_truefalse')
    question_based = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses_truefalse')
    answer_based = models.BooleanField()


class UserResponseModelFreeTextOption(models.Model):
    user = models.ForeignKey(UserINFO, on_delete=models.CASCADE, related_name='user_freetext')
    question_based = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses_freetext')
    answer_based = models.TextField(max_length=300)


class UserTimePassed(models.Model):
    started_time = models.DateTimeField(auto_now_add=True)
    ended_time = models.DateTimeField()



