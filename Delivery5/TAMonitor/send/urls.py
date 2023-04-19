from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.index),
    path('form/', views.send_email),


]