from rest_framework import status
from rest_framework.views import Response, APIView
import rest_framework.generics
from .models import Recipe
from .serializers import (RecipeCreateSerializers, RecipeListSerializers,
                          RecipeDetailSerializers, RecipeUpdateSerializers)


class RecipeListView(APIView):
    def get(self, request):
        recipe = Recipe.objects.all()
        serializers = RecipeListSerializers(recipe, many=True)
        return Response(serializers.data)


class RecipeDetailView(APIView):
    def get(self, request, pk):
        recipe = Recipe.objects.filter(id=pk).first()
        serializer = RecipeDetailSerializers(recipe)
        return Response(serializer.data)