from django.conf import settings

from .models import Category
from cart.utils import get_cart_message


def menu_items(request):
    context = {'is_authenticated': request.user.is_authenticated,
               'account_name': request.user.username if request.user.is_authenticated else 'Гость',
               'lot': get_cart_message(request),
               'categories_menu': Category.objects.filter(parent=None).order_by('-id')}

    return context
