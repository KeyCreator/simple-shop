from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView


from .models import Cart, Order
from shop.models import Product


class CartListView(ListView):
    template_name = 'cart.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        try:
            order = Order.objects.get(user=self.request.user, is_paid=False)
        except Order.DoesNotExist:
            return

        return Cart.objects.filter(order=order).order_by('-id')

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super(CartListView, self).get(*args, **kwargs)


def cart_add(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        order = Order.objects.get(user=request.user, is_paid=False)
    except Order.DoesNotExist:
        order = Order.objects.create(user=request.user)

    product = Product.objects.get(id=product_id)

    if Cart.objects.filter(order=order, product=product).count():
        purchase = Cart.objects.get(order=order, product=product)
        purchase.count += 1
        purchase.save()
    else:
        Cart.objects.create(order=order, product=product, count=1)

    return redirect(request.META.get('HTTP_REFERER'))


def order_pay(request):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        order = Order.objects.get(user=request.user, is_paid=False)
    except Order.DoesNotExist:
        return HttpResponse(f'При обработке заказа возникла ошибка')

    order.is_paid = True
    order.save()

    template = 'empty_section.html'

    return render(request,
                  template,
                  context={'message': f'Заказ №{order.id} обработан'})
