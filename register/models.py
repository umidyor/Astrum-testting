from django.db import models
from django.core.validators import MinLengthValidator



class Regsiter_site(models.Model):
    full_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.username





