import datetime

# contrib contains the common functionality for web dev
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # This representation is used throughout Django's admin.
    def __str__(self):
        return self.question_text

    # This is needed since sorting by a function is not supported.
    @admin.display(boolean=True, ordering='pub_date', description='Published recently?')
    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
