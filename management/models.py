from django.db import models
from django.db.models import Count, Model
from django.contrib.auth.models import User
from datetime import datetime, date, timezone
# from django.core.validators import MaxValueValidator
import os
from django.conf import settings
# from rest_framework import serializers
from django.urls import reverse
# Create your models here.


Category = [
   ("compulsary", "compulsary"),
   ("voluntary", "voluntary")
]

available = [
    ("Yes", "Yes"),
    ("No", "No"),
]


class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=100, default='')
    Course_Code = models.CharField(max_length=50, default='0000')
    credits = models.IntegerField(default=0)
    category = models.BooleanField(choices=Category, default="voluntary")
    Description = models.TextField(max_length=200, default='')
    Course = models.CharField(max_length=100, default='')
    avalaible = models.BooleanField(choices=available, default="Yes")
#    total_spaces = models.IntegerField()
#    registered_students = models.ManyToManyField(to=User)
#    number_of_students = models.Count(registered_students)

    def __str__(self):
        return f'{self.name} Module in {self.Description}'

    def get_absolute_url(self):
        return reverse('management/module_details', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(primary_key=True, max_length=40, default='')
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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    registration_time = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.Module}'
