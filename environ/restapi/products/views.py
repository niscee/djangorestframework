from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# dashboard page.
def dashboard(request):
    context = {}
    return render(request, 'products/dashboard.html', context)



    