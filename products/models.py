from django.db import models

from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    """ Model to store different Categories with pluralised admin name
     and firendly name for user """

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name or self.name


class Event(models.Model):
    '''Model to store different event types in summer season'''

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Model to store all product details which may be important to users """
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    event = models.ForeignKey('Event', null=True, blank=True, on_delete=models.SET_NULL)
    event_dates = models.CharField(max_length=254)
    number_available = models.IntegerField(default=0)
    postcode = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    listing_image = ImageSpecField(source='image', processors=[ResizeToFill(300, 225)], format='JPEG')
    late_arrival = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    number_available = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    '''# TODO (defensive design adding to ensure no page urls added in error)
    image_url = models.URLField(max_length=1024, null=True, blank=True)'''

    def __str__(self):
        return self.name
