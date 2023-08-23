from django.http import HttpResponse
from django.shortcuts import render


from django.contrib.auth.decorators import login_required
def login_required_decorator(func):
    return login_required(func, login_url='login')

@login_required_decorator
def create_test(request):
    return HttpResponse('sasdasd')
# Create your views here.
