from collections.abc import Iterable
from django.db import models
from GenerateSecureKeys.GenerateSlug import generate_secure_slug
from TestingSystem.models import Test
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


class Availability(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    def __str__(self):
        return "time_managed"


class AssignLinkModel(models.Model):
    test_foreign = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="assign_link"
    )
    limit_time = models.OneToOneField(
        "LimitTime", on_delete=models.CASCADE, related_name="limit_time"
    )
    display_each_question = models.OneToOneField(
        "DisplayEachQuestion", on_delete=models.CASCADE, related_name="display"
    )
    test_completion = models.OneToOneField(
        "TestCompletionModel", on_delete=models.CASCADE, related_name="test_comp"
    )
    creator_email_send = models.OneToOneField(
        "CreatorEmailSendModel",
        on_delete=models.CASCADE,
        related_name="creator_email",
        default=None,
        null=True,
    )
    taker_email_send = models.OneToOneField(
        "TakerEmailSendModel",
        on_delete=models.CASCADE,
        related_name="taker_email",
        default=None,
        null=True,
    )
    assign_link_foreign = models.OneToOneField(
        Availability, on_delete=models.CASCADE, related_name="availability"
    )
    assign_name = models.CharField(max_length=50) 
    slug_field = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return "valid_secure"

    def save(self, *args, **kwargs):
        if not self.slug_field:
            self.slug_field = generate_secure_slug(*args)
        super().save(*args, **kwargs)


class LimitTime(models.Model):
    minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1440)], default=0)
    limited_datetime = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.limited_datetime.time()}'


from django.db import models

NUMBER_CHOICES = [(str(i), str(i)) for i in range(1, 11)]


class DisplayEachQuestion(models.Model):
    selected_number = models.CharField(max_length=2, choices=NUMBER_CHOICES)
    randomize = models.BooleanField(default=False)
    must_answer = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "display_seted"


class TestCompletionModel(models.Model):
    pass_mark = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    send_completed_message = RichTextUploadingField()
    send_not_completed_message = RichTextUploadingField()

    def __str__(self) -> str:
        return f"{self.pass_mark}%"


class SendOffOn(models.Model):
    off_or_no = models.BooleanField(default=True)


class CreatorEmailSendModel(models.Model):
    offno = models.OneToOneField(
        SendOffOn, on_delete=models.CASCADE, related_name="off_no"
    )
    email = models.EmailField()


class TakerEmailSendModel(models.Model):
    point = models.BooleanField(default=False)
    percentage = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    graded = models.BooleanField(default=False)
    Reveal_correct_Answer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.point}"
