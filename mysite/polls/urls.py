from django.urls import path
from . import views

urlppatterns = [
        path('', views.index, name='index')
        ]
