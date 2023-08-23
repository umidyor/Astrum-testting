from django.urls import path
from .views import *
urlpatterns=[
    path('create_test',create_test,name='create_test'),
]