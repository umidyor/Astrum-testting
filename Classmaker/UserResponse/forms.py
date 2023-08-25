from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import UserINFO


class RegistrationForm(ModelForm):
    class Meta:
        model = UserINFO
        fields = ['name', 'surname', 'email', 'number', 'ms_name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-name',
                'placeholder': 'Please write firstname',
                'required': 'true',
            }),
            'surname': TextInput(attrs={
                'class': 'form-surname',
                'placeholder': 'Please write surname',
                'required': 'true',
            }),
            'email': EmailInput(attrs={
                'class': 'form-email',
                'placeholder': 'Please write email',
                'required': 'true',
            }),
            'ms_name': TextInput(attrs={
                'class': 'form-ms',
                'placeholder': 'Please write Main Season',
                'required': 'true',
            })
        }
