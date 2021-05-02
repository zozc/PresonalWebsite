from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home_view(request):
    profilex=str(request.user)
    #return HttpResponse("Hello, world. You're at the home "+profilex)
    return (request,"home.html",{})

def about_view(request):
    return HttpResponse ("<h1> About Us</h1>")
    