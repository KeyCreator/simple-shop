from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from urllib.parse import urlencode

from .models import Product, Category
from .utils import get_products_paginator


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        products = Product.objects.filter(for_main=True).order_by('-id')
        product_objs, current_page, prev_page, next_page = get_products_paginator(request, products, 2)

        category_menu = Category.objects.filter(parent=None).order_by('-id')

        return render(request, self.template_name, context={
            'is_authenticated': request.user.is_authenticated,
            'account_name': request.user.username if request.user.is_authenticated else 'Гость',
            'products': product_objs,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        })


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get(self, request):

        products = Product.objects.all()
        product_objs, current_page, prev_page, next_page = get_products_paginator(request, products, 2)

        return render(request, self.template_name, context={
            'is_authenticated': request.user.is_authenticated,
            'account_name': request.user.username if request.user.is_authenticated else 'Гость',
            'products': product_objs,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        })
