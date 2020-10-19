from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import BlogPost



# register user.AC
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"user {username} has been registered!!")
            return redirect('login')
        else:
            messages.success(request, "something went wrong")     
        
    form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)
        

# login user.
def logIn(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd   = request.POST.get('password')
        user = authenticate(email=email, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'credentials didnt match.')

    form = LoginForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)  


# logout user.
@login_required(login_url='')
def logOut(request):
    logout(request)
    return redirect('login')
    


