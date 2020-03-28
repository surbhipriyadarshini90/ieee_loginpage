from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html', {'name' :'user'})

def signin(request):
    return render(request, "result.html")
