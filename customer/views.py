from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.template_name)