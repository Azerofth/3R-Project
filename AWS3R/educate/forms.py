from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Tags

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_description', 'post_image', 'post_tags', 'post_author']
