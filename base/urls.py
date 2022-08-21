from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-item/<str:pk>', views.editItem, name='edit-item'),
    path('remove-item/<str:pk>', views.removeItem, name='remove-item'),
]