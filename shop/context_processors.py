from django.conf import settings

from .models import Group
from cart.utils import get_cart_message


def menu_items(request):
    context = {'is_authenticated': request.user.is_authenticated,
               'account_name': request.user.username if request.user.is_authenticated else 'Гость',
               'lot': get_cart_message(request),
               'product_groups_list': Group.objects.all().order_by('position')}

    return context
