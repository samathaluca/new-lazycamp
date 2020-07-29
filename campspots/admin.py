from django.contrib import admin
from .models import Campspot, Category

# Model fields display in Campspot admin.

class CampspotAdmin(admin.ModelAdmin):
    list_display = (
        'postcode',
        'name',
        'date',
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
