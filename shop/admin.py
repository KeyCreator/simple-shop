from django.contrib import admin

from .models import Phone, Category, Clothes, Remark
from cart.models import Cart, Order


class CartInline(admin.TabularInline):
    model = Cart


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    ordering = ('category', )
    list_display = ('article', 'name', 'category', )
    search_fields = ('article', 'name', )
    list_filter = ('category', 'name', 'price', )

    #  TODO: Прошу помочь с выводом изображения в админку
    def icon_tag(self, obj):
        if not (obj.pk and obj.image):
            return ''
        return u'<img src="%s" />' % obj.image.url

    icon_tag.short_description = 'Icon'
    icon_tag.allow_tags = True
    readonly_fields = ('icon_tag',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'parent')
    search_fields = ('name', )
    list_filter = ('name', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('-pay_date', '-id')
    # https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#inlinemodeladmin-objects
    inlines = [
        CartInline,
    ]


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    ordering = ('-id',)


@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    ordering = ('-id',)