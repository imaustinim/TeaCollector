from django.db import models


class Tea(models.Model):
    name = models.CharField(max_length=30)
    tea_type = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=30, default="")
    origin = models.CharField(max_length=30, default="Unknown")


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField(default=0)
    measurement = models.CharField(max_length=30)
