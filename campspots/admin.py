from django.contrib import admin
from .models import Campspot, Category


class CampspotAdmin(admin.ModelAdmin):
    list_display = (
        'postcode',
        'name',
        'category',
        'price',
        'is_available',
        'county',
        'image',
    )

    ordering = ('county',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Campspot, CampspotAdmin)
admin.site.register(Category, CategoryAdmin)
