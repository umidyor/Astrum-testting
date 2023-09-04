from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'picture', 'description']

        widgets = {'title':forms.TextInput(attrs={
            'class':'title-name',}),
                'picture':forms.FileInput(attrs={
            'class':'picture'}),
                'description':forms.Textarea(attrs={
            'class':'description'
                })
            }
class PostSearchForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your search query',
            'style': 'border-radius: 5px;'
        })
    )
