from django.core.paginator import Paginator
from urllib.parse import urlencode


def get_products_paginator(request, products, count_on_page):

    paginator = Paginator(products, count_on_page)
    current_page = request.GET.get('page', 1)

    product_objs = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if product_objs.has_previous():
        prev_page = product_objs.previous_page_number()
        prev_page = '?%s' % urlencode({'page': prev_page})
    if product_objs.has_next():
        next_page = product_objs.next_page_number()
        next_page = '?%s' % urlencode({'page': next_page})

    return product_objs, current_page, prev_page, next_page