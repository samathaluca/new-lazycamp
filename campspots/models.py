from django.db import models

from django.contrib.auth.models import User


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
        return self.friendly_name


class Campspot(models.Model):
    """ Model to store all campspot details which may be important to users """
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    county = models.CharField(max_length=254)
    postcode = models.CharField(max_length=254)
    postal_district = models.CharField(max_length=254)
    first_line_address = models.CharField(max_length=254)
    address_town_or_city = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    arrive_anytime = models.BooleanField(default=True)
    arrive_dawn_to_dusk = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    dogs_welcome = models.BooleanField(default=False)
    wi_fi = models.BooleanField(default=True)
    good_phone_signal = models.BooleanField(default=True)
    electric = models.BooleanField(default=True)
    motorhome_service_point = models.CharField(max_length=254)
    nearest_toilet_and_shower = models.CharField(max_length=254)
    host_brief = models.TextField()
    bare_all = models.TextField()
    nearest_toilet_and_shower = models.CharField(max_length=254)
    public_transport_options = models.CharField(max_length=254)
    local_eatery_and_shop = models.CharField(max_length=254)
    campspot_email = models.EmailField()

    # TODO add date so help admin know when campspot was added.
    ''' TODO (add defensive design to stop bus user errors)
    image_url = models.URLField(max_length=1024,null=True, blank=True'''

    def __str__(self):
        return self.name
