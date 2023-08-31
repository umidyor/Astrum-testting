from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.cache import cache

import secrets
def login_required_decorator(func):
    return login_required(func, login_url='home')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("home")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        user2=authenticate(request,passwor=password,email=username)
        if user or user2:
            login(request, user)
            return redirect("home")
    if request.user.is_authenticated:
        return redirect("home")


    return render(request, 'login.html')


# @login_required_decorator
def home_page(request):
    return render(request, 'index.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

# def change_password(request,pk,token):
#     if request.POST:
#         print(request.POST["password"])
#         user=User.objects.get(pk=pk)
#         user.password=request.POST["password"]
#         user.save()
#         return HttpResponse("Sucssesfully changed your password")
#         return redirect("login")
#     return render(request,"change_password.html")
#
# def forgot_password(request):
#     if request.POST:
#         user_email_forgot_password=request.POST["email"]
#         user_exists=User.objects.filter(email=user_email_forgot_password)
#         if user_exists:
#             random_bytes = secrets.token_bytes(12)
#             random_token = secrets.token_hex(12)
#             user=User.objects.get(email=user_email_forgot_password)
#             user_pk=user.pk
#             random_bytes = secrets.token_bytes(12)
#             random_token = secrets.token_hex(12)
#             subject = 'Hi!'
#             message = f"""Your token is-> http://127.0.0.1:8000/change_password/{user_pk}/{random_token}!"""
#             from_email = 'umidyor007@gmail.com'
#             recipient_list = [f'{user_email_forgot_password}']
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         else:
#             return HttpResponse("Don't find email:(")
#
#     return render(request,"forgot_password.html")

def custom_404_page(request,exception):
    return render(request, '404.html', status=404)

def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache cleared successfully.")