from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("home")

def login(request):
    return HttpResponse("login")

# def signup(request):
#     return HttpResponse("sign up")

def community(request):
    return HttpResponse("community")

def report(request):
    return HttpResponse("report")