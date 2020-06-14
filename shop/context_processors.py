from django.conf import settings

from .models import Category, Cart

def menu_items(request):
    context = {}
    context['is_authenticated'] = request.user.is_authenticated
    context['account_name'] = request.user.username \
        if request.user.is_authenticated else 'Гость'
    context['categories_menu'] = Category.objects.filter(parent=None).order_by('-id')
    context['lot'] = sum(Cart.objects.filter(user=request.user).values_list('count', flat=True)) \
        if request.user.is_authenticated else ''

    return context