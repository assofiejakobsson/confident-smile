from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'image', 'rating')
    list_filter = ('category',)
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')

admin.site.register(Category, CategoryAdmin)
