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

