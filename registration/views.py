from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
"""
def registration(request):
    return HttpResponse("Welcome to  registration")



def mypage(request):
    template = loader.get_template('registration')
    return HttpResponse(template.render())
# Create your views here.
"""

def home (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())



def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def Register(request):
    template = loader.get_template('Register.html')
    return  HttpResponse(template.render())
def course(request):
    template = loader.get_template('course.html')
    return HttpResponse(template.render())


