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

# class UploadForm(forms.Form):
#     post_title = forms.CharField()
#     post_description = forms.CharField()
#     post_image = forms.FileField()
#     post_tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all().values_list('tags_name', flat=True))
#     post_author = forms.CharField()
        