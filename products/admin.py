from django.contrib import admin
from .models import Product, Category

# Model fields display in Product admin.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        # 'postcode',
        'name',
        'category',
        'price',
        'image',
        'is_available',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
