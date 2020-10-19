from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# dashboard page.
@login_required(login_url='/')
def dashboard(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'products/dashboard.html', context)



@login_required(login_url='/')
def search(request):
    title = request.POST['search']

    if title:
        posts = BlogPost.objects.filter(title__contains=title)
    else:
        posts = BlogPost.objects.all()  

    context = {'posts': posts}
    return render(request, 'products/dashboard.html', context) 
    