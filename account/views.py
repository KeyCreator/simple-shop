from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from .models import CustomUser


class AuthView(TemplateView):
    template_name = 'register.html'

    def post(self, request):

        if request.POST['password'] != request.POST['password2']:
            return render(request,
                          self.template_name,
                          {'invalid_password2': 'Пароль не совпал'})
        password = request.POST['password']

        email = request.POST['email']
        if CustomUser.objects.filter(email=email).count():
            return render(request,
                          self.template_name,
                          {'invalid_email': 'Пользователь с таким email существует'})

        user = CustomUser()
        user.username, user.email = email, email
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('/')


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
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
