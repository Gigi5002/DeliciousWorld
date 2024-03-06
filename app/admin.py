from django.contrib import admin
from .models import Recipe, Ingredients, Category, DishType

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Category)
admin.site.register(DishType)
