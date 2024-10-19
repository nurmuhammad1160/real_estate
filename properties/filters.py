from django_filters import rest_framework as filters
from .models import Property

class PropertyFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Property
        fields = ['price', 'bedrooms', 'bathrooms', 'property_type', 'wifi', 'washer', 'ac', 'smoking', 'host_language']
