from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.title}"
    content = models.TextField()
    # lastEditedDate = models.DateTimeField('date edited')