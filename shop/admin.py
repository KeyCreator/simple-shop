from django.contrib import admin

from .models import Product, Category

from cart.models import Cart, Order


class CartInline(admin.TabularInline):
    model = Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('category', )
    list_display = ('article', 'image', 'name', 'category', 'price', )
    search_fields = ('article', 'name', )
    list_filter = ('category', 'name', 'price', )
    inline = [CartInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    ordering = ('order', )
    list_display = ('order', 'product', 'count', )
    search_fields = ('order', 'product', )
    list_filter = ('order', 'product', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass