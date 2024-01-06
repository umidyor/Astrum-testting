from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import handler404



urlpatterns = [
    path('',home_page, name='home'),
    path('login/',login_page, name='login'),
    path('logout/',logout_page, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="change_password.html"), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('clear_cache',clear_cache,name='clear_cache'),


]
#
handler404 = views.custom_404_page
