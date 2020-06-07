from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .models import CustomUser


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        print('POST - Я здесь')
        context = {}

        try:
            username = CustomUser.objects.get(email=request.POST['email'])
        except CustomUser.DoesNotExist:
            context['invalid_email'] = 'Несуществующий email'
            return render(request, self.template_name, context)

        user = authenticate(username=username, password=request.POST['password'])
        print(request.POST['email'], request.POST['password'])
        if user:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                context['invalid_email'] = 'Пользователь заблокирвоан'
        else:
            context['invalid_email'] = 'Неверный пароль'

        return render(request, self.template_name, context)
