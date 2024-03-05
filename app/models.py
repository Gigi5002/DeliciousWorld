from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=500)
    description = models.TextField()
    ingredients = models.ForeignKey('Ingredients', on_delete=models.PROTECT)
    cooking_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    dish_type = models.ForeignKey('DishType', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Ingredients(models.Model):
    name = models.CharField(max_length=500)
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=500)


class Category(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()


class DishType(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
