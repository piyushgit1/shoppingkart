from django.contrib import admin
from .models import Product, Variation
from django.db import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ('is_active',)

admin.site.register(Variation, VariationAdmin)

# Register your models here.
