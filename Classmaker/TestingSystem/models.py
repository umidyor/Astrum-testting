from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

import re
import unicodedata
from django.utils.text import slugify
import uuid

from django.urls import reverse


def generate_slugs(text):
    # Convert the text to lowercase
    text = text.lower()

    # Replace spaces and special characters with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)

    # Remove diacritics (accents and other marks)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

    hash_value = str(uuid.uuid4()).split('-')[-1]

    return f"{slugify(text)}-{hash_value}"


class Test(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=False, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slugs(self.description)
        super().save(*args, **kwargs)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = RichTextUploadingField(blank=True, null=True)
    ranking = models.PositiveIntegerField()
    slug = models.SlugField(unique=False, max_length=200)

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
