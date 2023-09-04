from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from GenerateSecureKeys.GenerateSlug import generate_slugs


class Test(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=200)
    testCreatedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slugs(self.title)
        super().save(*args, **kwargs)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = RichTextUploadingField(blank=True, null=True)
    ranking = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slugs(*args)
        super().save(*args, **kwargs)


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    answer = RichTextUploadingField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class TrueFalse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='truefalse')
    false = models.BooleanField(default=False)
    true = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question}"


class FreeText(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='freetext')
    freetext = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.freetext
