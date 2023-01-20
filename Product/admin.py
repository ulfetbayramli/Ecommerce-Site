from django.contrib import admin
from .models import Category, Color, Image, Manufacturer, Product, Product_version, Review

class ProductInline(admin.TabularInline):
    model = Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_navbar', 'p_category']
    list_filter = ['is_navbar']
    search_fields = ['name', 'p_category__name']
    empty_value_display = 'unknown'
    inlines = [ProductInline, ]

class ProductVersionInline(admin.TabularInline):
    model = Product_version
    exclude = ['review_count', 'read_count']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'category']
    list_filter = ['manufacturer', 'category']
    search_fields = ['price', 'new_price']
    empty_value_display = 'unknown'
    inlines = [ProductVersionInline, ]

@admin.register(Product_version)
class Product_VersionAdmin(admin.ModelAdmin):
    list_display = ['product', 'color']
    list_filter = ['color']
    search_fields = ['color']
    empty_value_display = 'unknown'


# admin.site.register(product_version)

admin.site.register(Image)
admin.site.register(Review)
admin.site.register(Manufacturer)
admin.site.register(Color)
