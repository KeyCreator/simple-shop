from django.urls import path

from .views import CartListView, cart_add, order_pay


urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart'),
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('order_pay/', order_pay, name='order_pay'),
]
