from django.db import models
from UserResponse.models import UserINFO

# Create your models here.

class UserResponseScore(models.Model):
    user = models.ForeignKey(UserINFO, on_delete=models.CASCADE, related_name='user_score')
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.score}'



