from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        print(self.cleaned_data)
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            return self.cleaned_data["username"]
        else:
            return email
