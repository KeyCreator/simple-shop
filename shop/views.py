from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        context = {}
        context['is_authenticated'] = request.user.is_authenticated
        context['account_name'] = request.user.username if request.user.is_authenticated else 'Гость'

        return render(request, self.template_name, context)