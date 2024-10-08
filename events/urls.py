from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='event_list'),
    # path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
]