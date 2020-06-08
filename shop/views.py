from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        context = {}
        context['is_authenticated'] = request.user.is_authenticated
        context['account_name'] = request.user.username if request.user.is_authenticated else 'Гость'

        return render(request, self.template_name, context)


class SmartphoneView(TemplateView):
    template_name = 'smartphones.html'

    def get(self, request):
        context = {}
        context['is_authenticated'] = request.user.is_authenticated
        context['account_name'] = request.user.username if request.user.is_authenticated else 'Гость'

        return render(request, self.template_name, context)