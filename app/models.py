from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    name=models.CharField(max_length=10,default=None)
    roll_no = models.IntegerField(default=0)
    dept = models.ForeignKey('Department',on_delete=models.CASCADE,related_name='dept',default=None)
    books = models.ManyToManyField('Books',related_name='books',default=None)
    def __str__(self):
        return str(self.name)

class Department(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return str(self.name)

class Books(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return str(self.name)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=10)
        
    def __str__(self):
        return str(self.name)