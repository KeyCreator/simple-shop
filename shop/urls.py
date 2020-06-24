from django.urls import path

from .views import HomeView, CategoryView, ProductDetailView, remark_add


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product'),
    path('feedback/<int:product_id>/', remark_add, name='feedback'),
]