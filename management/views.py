from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from .models import Module, Registration, Course
from django.http import HttpResponse
from .forms import RegistrationForm, ModuleForm, CourseForm
from django.contrib.auth.models import User
from itapps import settings
from django.urls import reverse_lazy
# Create your views here.


@login_required
def welcome(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
    cities = [('Sheffield', 'UK'), ('Melaka', 'Malaysia'), ('Bandung', 'Indonesia')]
    weather_data = []
    api_key = 'de13554a89154438878bf77424a0ca05'

    for city in cities:
        city_weather = requests.get(url.format(city[0], city[1], api_key)).json() # Request the API data and convert the JSON to Python data types

    weather = {
        'city': city_weather['name'] + ', ' + city_weather['sys']['country'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description']
    }
    weather_data.append(weather)  # Add the data for the current city into our list

    return render(request, 'management/welcome.html', {'title': 'Welcome', 'weather_data': weather_data})


def Courses(request):
    return render(request, 'management/courses.html', {'title': 'Courses'})


@login_required
def module_list(request):
    modules = Module.objects.all()
    context = {'modules': modules}
    return render(request, 'management/module_list.html', context)


class ModuleView(DetailView):
    model = Module
    fields = ['Name', 'Course_Code', 'credits', 'Category', 'Description',
              'Course', 'available']

    @login_required
    def Module_detail(request, Module):
        Module.objects.get()
        if request.method != "POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
        else:
            Module.name = request.POST.get('Name')
            Module.Course_Code = request.POST.get('Course Code')
            Module.credits = request.POST.get('credits')
            Module.Category = request.POST.get('Category')
            Module.Description = request.POST.get('Description')
            Module.Course = request.POST.get('Course')
            Module.availabile = request.POST.get('availability')
        return render(request, "management/module_details")


@login_required
def Registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, user=request.user)  # Pass the current logged-in user
        if form.is_valid():
            form.save()  # Save the registration
            return redirect('module_success')  # Redirect to a success page
    else:
        form = RegistrationForm(user=request.user)  # Pass the user to the form

    return render(request, 'management/registration', {'form': form})


def success_view(request):
    return render(request, 'success.html')


class AddModuleView(CreateView):
    model = Module
    fields = ['Name', 'Course_Code', 'credits', 'Category', 'Description',
              'Course', 'available']

    @login_required
    def add_module(self, form, request):
        if request.method == 'POST':
            form = ModuleForm(request.POST or None)
        if form.is_valid():
            form.save()  # Save the module to the database
            return redirect(request, 'add_module')  # Redirect to the module list page or any other page
        else:
            form = ModuleForm()

        return render(request, 'add_module', {'form': form})


class AddCourseView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['name', 'module']
    template_name = 'management/add_course.html'
    success_url = reverse_lazy('management/module_list')  # Redirect to the module list page or any other page
    
    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user  # Assuming you want to associate the course with the logged-in user
        return super().form_valid(form)


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'management/course_list.html', {'courses': courses})
