from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

DRINKS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('S', 'Snack'),
    ('D', 'Dinner'),
)


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk': self.id})


class Tea_Type(models.Model):
    class Name(models.TextChoices):
        GreenTea = 'Gre', "Green Tea"
        BlackTea = 'Bla', "Black Tea"
        WhiteTea = 'Whi', "White Tea"
        Jasmine = "Jas", "Jasmine"
        Oolog = "Ool", "Oolong"
        Matcha = "Mat", "Matcha"
        Chai = "Cha", "Chai"
        Rooibos = "Roo", "Rooibos"
        Herbal = "Her", "Herbal"
        Fruit = "Fru", "Fruit"

    name = models.CharField(max_length=30, choices=Name.choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tea_detail', kwargs={'pk': self.id})


class Tea(models.Model):
    name = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    tea_type = models.ManyToManyField(Tea_Type)
    ingredients = models.ManyToManyField(Ingredients)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # tea_type = models.CharField(max_length=30, choices=Tea_Types.choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def drinks(self):
        return self.drink_set.filter(date=date.today()).count()

    def getPercentage(self):
        count = self.drink_set.filter(date=date.today()).count()
        return round(count / (count+10) * 100, 2)

    def drank_today(self):
        return self.drink_set.filter(date=date.today()).count() >= len(DRINKS)


class Drink(models.Model):
    date = models.DateField('drink date')
    drink = models.CharField(
        max_length=1,
        choices=DRINKS,
        default=DRINKS[0][0]
    )
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_drink_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for tea_id: {self.tea_id} @{self.url}"
