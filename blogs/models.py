from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


def get_default_author():
    return User.objects.first()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)  # Make sure this line is correct
    picture = models.ImageField(upload_to="post_image_upload_path")
    slug = models.SlugField(max_length=200)
    publish = models.DateTimeField(default=datetime.now)
    description = models.TextField()





    def __str__(self):
        return self.title

    class Meta:
        ordering=['-publish']
        indexes=[
            models.Index(fields=['-publish'])
        ]

class Edd(models.Model):
    # class SeasonChoices(models.IntegerChoices):
    #     MS4 = 4, 'MS4'
    #     MS5 =5, 'MS5'
    #     MS6 =6, 'MS6'
    #     MS7 =7, 'MS7'
    #     MS8 =8, 'MS8'
    #     MS9 =9, 'MS9'
    #     MS10 =10, 'MS10'
    #     MS11 =11, 'MS11'
    #     MS12 =12, 'MS12'

    full_name=models.CharField(max_length=200)
    season=models.CharField(max_length=10)
    phone_number=models.BigIntegerField()
    post_id=models.CharField(max_length=20)


    def __str__(self):
        return self.full_name
