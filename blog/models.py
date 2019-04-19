from django.db import models
from django.urls import reverse

# Create your models here.


class Article (models.Model):
    title	= models.CharField(max_length=313)
    content = models.TextField()
    active	= models.BooleanField(default=True)

    def get_absolute_url(self):
    	return reverse("article:article-detail", kwargs={"id": self.id})