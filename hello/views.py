from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")#hello is a folder in template folder

def brian(request):
    return HttpResponse("hello brian")
"""
def greet(request,name):
    return HttpResponse(f"hello,{name}!!")
    """
def greet(request,name):
    return render(request,"hello/greet.html",{"name":name.capitalize()})