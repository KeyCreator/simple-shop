from django.urls import path

from .views import HomeView, CategoryView, ProductDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product'),
]