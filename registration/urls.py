from django.urls import path
from . import views


urlpatterns = [
#   path('registration/', views.registration, name='registration'),

   path('login/', views.login, name=' myloginpage'),
   path('home/', views.home, name='homepage'),
   path('about/', views.Register, name='Register'),
   path('course/', views.course, name='course')
]