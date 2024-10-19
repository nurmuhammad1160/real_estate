from django.shortcuts import render

from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PropertyFilter

# class PropertyListCreate(generics.ListCreateAPIView):
#     queryset = Property.objects.all()
#     serializer_class = PropertySerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['price', 'bedrooms', 'bathrooms', 'property_type', 'wifi', 'washer', 'ac', 'smoking', 'host_language']


class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter  # Yangi filtr klassini qo'shish