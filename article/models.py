from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=250)
    article_text = models.CharField(max_length=5000)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk) + "-" + self.article_title
