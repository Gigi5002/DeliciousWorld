from rest_framework import status
from rest_framework.views import Response, APIView
import rest_framework.generics
from .models import Recipe
from .serializers import (
    RecipeCreateSerializers, RecipeListSerializers,
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

    def patch(self, request, pk):
        recipe = rest_framework.generics.get_object_or_404(Recipe.objects.all(), id=pk)
        serializer = RecipeUpdateSerializers(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = rest_framework.generics.get_object_or_404(Recipe.objects.all(), id=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeCreateView(APIView):
    def post(self, request):
        serializer = RecipeCreateSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
