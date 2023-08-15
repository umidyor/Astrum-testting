from django.urls import path
from .views import register,login_,logout_view,send_test_email,forgot_password,change_password,home  # Import the view function or class from the test app

urlpatterns = [
    path('',home,name='home'),
    path('register', register, name="register"),  # Example URL pattern for testing
    path('login',login_,name="login"),
    path('logout',logout_view,name='logout'),
    path('sent',send_test_email,name='sent'),
    path('forgot',forgot_password,name="forgot"),
    path('change_password/<int:pk>/<str:token>',change_password,name="change_password")
    # Define other URL patterns for the test app here
]

