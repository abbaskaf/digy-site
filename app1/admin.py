from django.contrib import admin
from .models import Product, Image, Category, Costumer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'is_discount', 'price')
    list_filter = ('brand', 'category', 'is_discount')
    list_per_page = 10


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone', 'product')
    list_filter = ('product',)
    list_per_page = 10


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_filter = ('product',)
