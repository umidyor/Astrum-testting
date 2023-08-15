from .models import Regsiter_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import secrets

def login_required_decorator(f):
    return login_required(f,login_url='login')


# Create your views here.
def register(request):
    if request.POST:
        try:
            analyse = Regsiter_site.objects.get(email=request.POST['email'])
            return HttpResponse(f"Afsuski bu {request.POST['email']} akauntiga akaunt ochilgan!")

        except:
            model = Regsiter_site()
            model.full_name = request.POST['full_name']
            model.username = request.POST['username']
            model.email = request.POST['email']
            model.password = request.POST['password']
            model.save()
            return redirect('login')
    return render(request, "register.html")


# views.py


from django.core.mail import send_mail
from django.shortcuts import render


def send_test_email(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,"email_sent.html")




# def forgot_password(request, user):
#     if request.POST:
#         user_email_for_password = request.POST["email"]
#         print(user_email_for_password)
#         user_exists = Regsiter_site.objects.filter(email=user_email_for_password)
#         if user_exists:
#             random_bytes = secrets.token_bytes(12)
#             random_token = secrets.token_hex(12)
#             subject = 'Hi!'
#             message = f"""Your token is-> {random_token}!"""
#             from_email = 'umidyor007@gmail.com'
#             recipient_list = [f'{user_email_for_password}']
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#             return redirect("sent")
#
#
#         else:
#             return HttpResponse(
#                 f"Sizning ushbu {user_email_for_password} akauntingiz topilmadi iltimos qayta ro'yxatdan o'ting:(")
#
#     return render(request, "forgot_password.html")

def change_password(request,pk,token):
    if request.POST:

        user=Regsiter_site.objects.get(pk=pk)
        user.password=request.POST["token"]
        user.save()
        return HttpResponse("Sucssesfully changed your password")
        return redirect("login")
    return render(request,"email_sent.html")

def forgot_password(request):
    if request.POST:
        user_email_forgot_password=request.POST["email"]
        user_exists=Regsiter_site.objects.filter(email=user_email_forgot_password)
        if user_exists:
            random_bytes = secrets.token_bytes(12)
            random_token = secrets.token_hex(12)
            user=Regsiter_site.objects.get(email=user_email_forgot_password)
            user_pk=user.pk
            random_bytes = secrets.token_bytes(12)
            random_token = secrets.token_hex(12)
            subject = 'Hi!'
            message = f"""Your token is-> http://127.0.0.1:8000/change_password/{user_pk}/{random_token}!"""
            from_email = 'umidyor007@gmail.com'
            recipient_list = [f'{user_email_forgot_password}']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    return render(request,"forgot_password.html")








def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_exists = Regsiter_site.objects.filter(username=username, password=password).exists()
        if user_exists:
            return redirect("logout")
        else:
            return redirect("register")

    return render(request, 'login.html')



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('register')  # Replace 'home' with the appropriate URL name
    else:
        return redirect('forgot')


def home(request):
    return render(request,"home.html")