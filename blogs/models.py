from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

def get_default_author():
    return User.objects.first()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)  # Make sure this line is correct
    picture = models.ImageField(upload_to="post_image_upload_path")
    slug = models.SlugField(max_length=200)
    publish = models.DateTimeField(default=datetime.now)
    description = models.TextField()

    def get_absolute_url(self):
        # Use the 'posts' URL pattern name with appropriate arguments
        return reverse('posts', args=[str(self.id), self.slug])
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         # If custom_id is not set, assign the next available integer
    #         last_record = Post.objects.last()
    #         if last_record:
    #             self.pk = last_record.pk + 1
    #         else:
    #             # If there are no existing records, start from 1
    #             self.pk = 1
    #     super().save(*args, **kwargs)



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

    custom_id = models.PositiveIntegerField(primary_key=True, unique=True)
    full_name=models.CharField(max_length=200)
    season=models.CharField(max_length=10)
    phone_number=models.BigIntegerField()
    post_id=models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.custom_id:
            # If custom_id is not set, assign the next available integer
            last_record = Edd.objects.last()
            if last_record:
                self.custom_id = last_record.custom_id + 1
            else:
                # If there are no existing records, start from 1
                self.custom_id = 1
        super().save(*args, **kwargs)


    def __str__(self):
        return self.full_name
