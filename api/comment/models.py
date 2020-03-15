from django.db import models
from django.contrib.auth.models import User
from api.article.models import Article

class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()
