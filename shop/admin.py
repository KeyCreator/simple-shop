from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Phone, Category, Group, Clothes, Remark


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    ordering = ('category', )
    list_display = ('article', 'name', 'category', )
    search_fields = ('article', 'name', )
    list_filter = ('category', 'name', 'price', )

    def icon_tag(self, obj):
        if not (obj.pk and obj.image):
            return ''
        return mark_safe('<img src="%s" />' % obj.image.url)

    icon_tag.short_description = 'Icon'
    icon_tag.allow_tags = True
    readonly_fields = ('icon_tag',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'group')
    search_fields = ('name', )
    list_filter = ('name', )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ('position',)
    list_display = ('name', 'position')
    search_fields = ('name', )


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    ordering = ('-id',)


@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    ordering = ('-id',)
