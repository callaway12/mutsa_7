from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('', blogapp.views.home, name='home'),
]
