from django.db import models


class Student(models.Model):
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   date_of_birth = models.DateField()
   email = models.EmailField(unique=True)
   phone_number = models.CharField(max_length=15, blank=True, null=True)
   address = models.TextField(blank=True, null=True)



class Pupils(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField(null=False, blank=False)
    Email = models.EmailField(unique=True)

