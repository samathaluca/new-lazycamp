from django.db import models

from django.contrib.auth.models import User

# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name or self.name


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    pitch_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    lateArrival = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    # listing_image = ImageSpecField(source='image', processors=[ResizeToFill(300, 225)], format='JPEG')

    # number_available = models.IntegerField(default=0)

    def __str__(self):
        return self.name
