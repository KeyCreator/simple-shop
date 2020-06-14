from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from urllib.parse import urlencode

from .models import Product, Category, Cart
from .utils import get_products_paginator
from .forms import PhoneForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        products = Product.objects.filter(for_main=True).order_by('-id')
        product_objs, current_page, prev_page, next_page = get_products_paginator(request, products, 2)

        return render(request, self.template_name, context={
            'products': product_objs,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        })


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get(self, request, category_id):

        try:
            category = Category.objects.get(id=category_id)
        except Poll.DoesNotExist:
            raise Http404("Category does not exist")

        products = Product.objects.filter(category=category)
        product_objs, current_page, prev_page, next_page = get_products_paginator(request, products, 2)

        return render(request, self.template_name, context={
            'category_name': category.name,
            'products': product_objs,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        })


class CartListView(ListView):
    template_name = 'cart.html'
    # model = Cart
    context_object_name = 'purchases'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).order_by('-id')

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super(CartListView, self).get(*args, **kwargs)


def cart_add(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(id=product_id)
    if Cart.objects.filter(user=request.user, product=product).count():
        cart = Cart.objects.get(user=request.user, product=product)
        cart.count += 1
        cart.save()
    else:
        Cart.objects.create(user=request.user, product=product, count=1)

    return redirect(request.META.get('HTTP_REFERER'))


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
