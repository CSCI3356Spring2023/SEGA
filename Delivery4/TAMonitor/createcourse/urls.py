from django.urls import path
from . import views

urlpatterns = [
    path('createcourse/', views.members, name='createcourse'),
]

