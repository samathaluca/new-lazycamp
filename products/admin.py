from django.contrib import admin
from .models import Product, Category, Event

# Model fields display in Product admin.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        # date enable keeps check on recently added events easily in admin
        'date',
        'event',
        'category',
        'price',
        'is_available',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
