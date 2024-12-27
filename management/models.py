from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
# from django.utils import 
from datetime import datetime, date
# from django.core.validators import MaxValueValidator
import os
from django.conf import settings
# from rest_framework import serializers

# Create your models here.


Category = [
   ("compulsary", "voluntary"),
   ("voluntary", "voluntary")
]

available = [
    ("Yes", "Yes"),
    ("No", "No"),
]


class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=100),
    Course_Code = models.CharField(max_length=50),
    credits = models.IntegerField(),
    category = models.BooleanField(choices=Category),
    Description = models.TextField(max_length=200),
    Course = models.CharField(max_length=100),
    avalaible = models.BooleanField(choices=available),
#    total_spaces = models.IntegerField(),
#    registered_students = models.ManyToManyField(to=User),
#    number_of_students = models.Count(registered_students)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    name = models.CharField(primary_key=True, max_length=40),
    module = models.ForeignKey(to=Module, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self}'


class ContactSubmission(models.Model):
    todaysDate = models.DateField(auto_now_add=True, null=True)
    name = models.CharField(max_length=20, default='N/A')
    email = models.EmailField(max_length=20, default='')
    subject = models.CharField(max_length=50, default='')
    message = models.TextField(max_length=300, default='')

    def __str__(self):
        return f'{self.todaysDate} - {self.subject}'


class Registration(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    todaysDate = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.student} - {self.Module}'
