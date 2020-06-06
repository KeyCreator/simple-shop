from django.contrib import admin

from .models import Product, Category
# from .forms import ReviewAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('category', )
    list_display = ('article', 'image', 'name', 'category', 'price', )
    search_fields = ('article', 'name', )
    list_filter = ('category', 'name', 'price', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )

    # form = ReviewAdminForm