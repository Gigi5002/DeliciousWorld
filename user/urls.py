from django.urls import path
from . import views

urlpatterns = [
    path('user_list/', views.UserListView.as_view()),
    path('register/', views.UserCreateView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
]
