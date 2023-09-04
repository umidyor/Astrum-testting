from django.db import models
from GenerateSecureKeys.GenerateSlug import generate_secure_slug
from TestingSystem.models import Test


class Availability(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    def __str__(self):
        return 'time_managed'


class AssignLinkModel(models.Model):
    test_foreign = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='assign_link')
    assign_link_foreign = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name='availability')
    slug_field = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return 'valid_secure'

    def save(self, *args, **kwargs):
        if not self.slug_field:
            self.slug_field = generate_secure_slug(*args)
        super().save(*args, **kwargs)



from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

