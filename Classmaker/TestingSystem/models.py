from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import random
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

class TestQuestionRandomize(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_random')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_random')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('test', 'question')

    def __str__(self):
        return self.question.text

    @classmethod
    def randomize_questions(cls, test_instance):
        questions = list(test_instance.questions.all())
        random.shuffle(questions)
        for index, question in enumerate(questions):
            test_question, created = cls.objects.get_or_create(test=test_instance, question=question)
            test_question.order = index + 1
            test_question.save()


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
