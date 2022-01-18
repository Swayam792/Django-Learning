from django.contrib import admin
from django.urls import path,include
from .views import CustomUserCreate
 
urlpatterns = [
    path('register/', CustomUserCreate.as_view(),name="create_user"),
     
]

app_name = 'users'