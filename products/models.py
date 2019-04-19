from django.db import models
from django.urls import reverse

# Create your models here.
class Product (models.Model):
    title       = models.CharField(default='this is cool!', max_length=200)
    description = models.TextField(default='Description')
    price       = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    summary     = models.TextField(default='Summary')

    def get_absolute_url(self):
    	return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"