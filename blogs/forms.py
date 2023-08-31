from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'picture', 'description']

class PostSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label='Search')