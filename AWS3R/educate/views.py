from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print(f"Welcome, {username}")
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('main')

def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            new_user1 = User.objects.create_user(
                    username=username,
                    password=password,  
                )
            new_user1.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration.html', {'form': form})

def main(request):
    posts = Post.objects.all()
    # Pass the retrieved posts to the template context
    context = {'posts': posts}
    # Render the template with the context data
    return render(request, 'main.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'readpost.html', {'post': post})

def upload(request):
    tags = Tags.objects.all()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['post_title']
            description = form.cleaned_data['post_description']
            image = form.cleaned_data['post_image']
            tags = form.cleaned_data['post_tags']
            author = form.cleaned_data['post_author']
            new_post = Post.objects.create(
                post_title = title,
                post_description = description,
                post_image = image,
                post_tags = tags,
                post_author = author
            )
            new_post.save()
            return redirect('main')
    else:
        form = UploadForm()    
    return render(request, 'upload.html', {'form': form, 'tags': tags})



             






            
