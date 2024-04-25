from django.urls import path
from . import views


urlpatterns = [
#   path('registration/', views.registration, name='registration'),

   path('login/', views.login, name=' myloginpage'),
   path('home/', views.home, name='homepage'),
   path('about/', views.Register, name='Register'),
   path('course/', views.course, name='course'),
   path('', views.home, name='myhome'),
   path('Register/', views.Register, name='Table'),

   path('addstudent', views.addstudent, name='addingstudent'),
   path('editstudent/<id>', views.editstudent, name='editstudent'),
   path('updatestudent/<id>', views.updatestudent, name='updatestudent'),
   path('deletestudent/<id>', views.deletestudent)

]


