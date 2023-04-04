from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.members, name='summary'),
]

