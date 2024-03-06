from django.urls import path
from .views import RecipeDetailView, RecipeListView, RecipeCreateView


urlpatterns = [
    path('recipe_list/', RecipeListView.as_view()),
    path('recipe_detail/<int:pk>', RecipeDetailView.as_view()),
    path('recipe_create/', RecipeCreateView.as_view())
]
