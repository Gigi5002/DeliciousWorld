from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='автор')
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    ingredients = models.ForeignKey('Ingredients', on_delete=models.PROTECT, verbose_name='ингредиенты')
    cooking_time = models.DateTimeField(auto_now_add=True, )
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категории блюд')
    dish_type = models.ForeignKey('DishType', on_delete=models.PROTECT, verbose_name='типы блюд')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Ingredients(models.Model):
    name = models.CharField(max_length=500, verbose_name='название')
    quantity = models.IntegerField(default=1, blank=True, null=True, verbose_name='количество')
    unit = models.CharField(max_length=500, verbose_name='единица', help_text='единица измерения (грамм, литр)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Category(models.Model):
    title = models.CharField(max_length=500, verbose_name='название', help_text='категории блюд (завтрак, обед, ужин)')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class DishType(models.Model):
    title = models.CharField(
        max_length=500, verbose_name='название',
        help_text='типы блюд (первое, второе, напитки, десерт)')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Типы блюд'
        verbose_name_plural = 'Типы блюд'
