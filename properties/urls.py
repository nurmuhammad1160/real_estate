from django.urls import path
from .views import PropertyListCreate

urlpatterns = [
    path('properties/', PropertyListCreate.as_view(), name='property-list-create'),
]
