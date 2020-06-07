from django.contrib import admin
from .models import CustomUser
# from .forms import ReviewAdminForm


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    pass
    # form = ReviewAdminForm


