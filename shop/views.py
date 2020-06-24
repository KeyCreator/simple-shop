from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from urllib.parse import urlencode

from .models import Product, Category, Phone, Clothes, Remark
from .utils import get_products_paginator
from .forms import ProductForm

from cart.models import Cart


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        phones = Phone.objects.filter(for_main=True).order_by('-id')
        phone_objs, phones_current_page, phones_prev_page, phones_next_page = \
            get_products_paginator(request, phones, 2)

        clothes = Clothes.objects.all().order_by('-id')
        clothes_objs, clothes_current_page, clothes_prev_page, clothes_next_page = \
            get_products_paginator(request, clothes, 2)

        return render(request, self.template_name, context={
            'phones': phone_objs,
            'phones_current_page': phones_current_page,
            'phones_prev_page_url': phones_prev_page,
            'phones_next_page_url': phones_next_page,
            'clothes': clothes_objs,
            'clothes_current_page': clothes_current_page,
            'clothes_prev_page_url': clothes_prev_page,
            'clothes_next_page_url': clothes_next_page,
        })


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get(self, request, slug):

        # slug = request.GET.get('slug')
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404("Такой категории товаров не существует")

        phones = Phone.objects.filter(category=category)
        phone_objs, current_page, prev_page, next_page = get_products_paginator(request, phones, 2)

        return render(request, self.template_name, context={
            'category_name': category.name,
            'phones': phone_objs,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        })


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

def remark_add(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
    except Order.DoesNotExist:
        return render(request, 'empty_section.html', {'message': f'Ошибка: Товар id={product_id} не найден'})

    if Remark.objects.filter(session_id=request.session.session_key, product=product).count():
        remark = Remark.objects.get(session_id=request.session.session_key, product=product)
    else:
        remark = Remark()
        remark.session_id = request.session.session_key
        remark.product = product

    remark.name = request.POST['name']
    remark.content = request.POST['description']
    remark.estimation = request.POST['mark']

    remark.save()

    return redirect(request.META.get('HTTP_REFERER'))
