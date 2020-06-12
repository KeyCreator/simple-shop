"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authViews

from shop.views import HomeView, CategoryView, CartView, cart_add
from account.views import LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),

]
