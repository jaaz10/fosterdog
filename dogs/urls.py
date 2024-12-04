from django.urls import path
from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.dog_list, name='dog_list'),
    path('add/', views.add_dog, name='add_dog'),
    path('edit/<int:pk>/', views.edit_dog, name='edit_dog'),
]
