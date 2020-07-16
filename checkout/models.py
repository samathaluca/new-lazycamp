from django.db import models
from django.db.models import Sum
# from django.conf import settings

from django_countries.fields import CountryField

from campspots.models import Campspot
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    night_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    beginner_tips = models.TextField(null=True, blank=True, default='')
    seasonned_tips = models.TextField(null=True, blank=True, default='')
    original_book = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    class Meta:
        ordering = ['-date']

    # def _generate_order_number(self):
    #     """
    #     Generate a random, unique order number using UUID
    #     """
    #     return uuid.uuid4().hex.upper()

    @property
    def grand_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        return self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """

        super().save(*args, **kwargs)
        if not self.order_number:
            self.order_number = self.date.strftime('%y%m%d') + str(self.pk)
            super().save()

    # def __str__(self):
    #     return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE,
                              related_name='lineitems')
    campspot = models.ForeignKey(Campspot, null=True, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    booking_date = models.DateTimeField(null=True)
    number_nights = models.IntegerField(null=True)
    pitch_sizes = models.CharField(max_length=2, null=True, blank=True) # bunk, S, M, L, XL
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


    # def clean(self):


    #     # Don't allow purchasing of more items than are in inventory


    #     if self.quantity > self.product.number_available:


    #         raise ValidationError(


    #             _('There aren\'t enough items to fulfil this order.'))




    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        # lineitem_total = self.product.price * self.quantity * self.number_nights
        # print(lineitem_total)
        self.lineitem_total = self.campspot.price * self.quantity * self.number_nights
        super().save(*args, **kwargs)

    def __str__(self):
        # return f'SKU {self.product.sku} on order {self.order.order_number}'
        
        return f'POSTCODE {self.campspot.postcode} on order {self.order.order_number}'




