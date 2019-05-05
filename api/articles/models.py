import datetime

from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')
    introduction = models.TextField()
    description = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
