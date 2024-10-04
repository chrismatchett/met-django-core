from django.urls import path
from . import views

urlpatterns = [
    path('', views.react_home, name='react_home'),
]