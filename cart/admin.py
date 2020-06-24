from django.contrib import admin

from .models import Cart, Order


class CartInline(admin.TabularInline):
    model = Cart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('-pay_date', '-id')
    # https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#inlinemodeladmin-objects
    inlines = [
        CartInline,
    ]


