from django.urls import path
from . import views

urlpatterns = [
    path('registercourse/', views.registercourse, name='registercourse'),
]

