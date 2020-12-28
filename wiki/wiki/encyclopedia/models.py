from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return f"{self.title}"
    content = models.TextField()
    # lastEditedDate = models.DateTimeField('date edited')

    # allows creation of new entry to redirect to new entry page
    # called by CreateView and UpdateView generic classes
    def get_absolute_url(self):
        return reverse("wiki:wiki-detail", kwargs={"wikiEntry": self.title})