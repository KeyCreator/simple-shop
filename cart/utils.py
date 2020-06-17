from .models import Cart, Order


def get_cart_message(request):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(user=request.user, is_paid=False)
        except Order.DoesNotExist:
            return ''
    else:
        return ''

    count = sum(Cart.objects.filter(order=order).values_list('count', flat=True))
    return f'({count})'