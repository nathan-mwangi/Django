from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Pupils

from registration.models import Pupils

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
    data = Pupils.objects.all()
    context = {'data': data}
    return render(request, 'Register.html')

def course(request):
    template = loader.get_template('course.html')
    return HttpResponse(template.render())

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        Name = request.POST.get('studname')
        Age = request.POST.get('studage')
        Email = request.POST.get('studemail')


    Student1=Pupils(Name=Name, Age=Age, Email=Email)
    Student1.save()

    data = Pupils.objects.all()
    context = {'data': data}
    return render(request, 'Register.html',context)


def editstudent(request, id):
    data = Pupils.objects.get(id=id),
    context = {'data': data}
    return render(request, 'updatestudent.html',context)


def updatestudent(request, id):
  if request.method == 'POST':
     Name = request.POST.get('studname')
     Age = request.POST.get('studmail')
     Email = request.POST.get('studage')

     editstudent = Pupils.objects.get(id=id)
     editstudent.Name = Name
     editstudent.Age = Age
     editstudent.Email = Email

     editstudent.save()
     data = Pupils.objects.all()
     context = {'data': data}
     return render(request, 'Register.html', context)

def deletestudent(request,id):
     deletestudent = Pupils.objects.get(id=id)
     deletestudent.delete()
     return redirect('/Register')


