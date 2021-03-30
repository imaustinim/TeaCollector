from django.db import models
from django.urls import reverse


class Tea(models.Model):
    name = models.CharField(max_length=30)
    tea_type = models.CharField(max_length=30)
    origin = models.CharField(max_length=30, default="Unknown")
    ingredients = models.CharField(max_length=30, default="Unknown")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tea_id': self.id})


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField(default=0)
    measurement = models.CharField(max_length=30)
