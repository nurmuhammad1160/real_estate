from django.db import models

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
    ]

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    property_type = models.CharField(choices=PROPERTY_TYPE_CHOICES, max_length=10)
    wifi = models.BooleanField(default=False)
    washer = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)  # air conditioning
    smoking = models.BooleanField(default=False)
    host_language = models.CharField(max_length=50)
    image_url = models.URLField()

    def __str__(self):
        return self.title
