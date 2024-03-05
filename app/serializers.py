from rest_framework import serializers
from .models import Recipe


class RecipeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateSerializers(serializers.ModelSerializer):
    class Meta:
        models = Recipe
        fields = '__all__'
