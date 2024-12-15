from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .forms import ModuleRegistrationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import requests
from .models import Module
from django.http import HttpResponse

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


class ModuleListView(ListView):
    url = 'https://registrationapp-sp2292.azurewebsites.net/api/modules/'
    Module_data = []
    template_name = 'management/module_list.html'
    context_object_name = 'Module'
    paginate_by = 5  # Optional pagination


@login_required
def Modulelist(request):
    modules = Module.objects.all(ListView)
    context = {"Name": modules}
    return render(request, "management/module_list.html", context)


@login_required
def Module_detail(request, Module):
    Module.objects.get()

    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:

        Module = request.POST.get('Name')
        Module.Course_Code = request.POST.get('Course Code')
        Module.credits = request.POST.get('credits')
        Module.Category = request.POST.get('Category')
        Module.Description = request.POST.get('Description')
        Module.Course = request.POST.get('Course')
        Module.availabile = request.POST.get('availability')
        if 'subscribe' in request.POST:
            User = request.POST.get("user")
            User.save()
            messages.info(request, 'You have successfully registered for {{Module.name}}')

        if 'unsubscribe' in request.POST:
            Module.objects.get(
            User = request.POST.get("user")).delete()
            messages.info(request, 'You are no longer registered for  {{Module.name}}')
        return render(request, "management/module_details")

"""
@login_required
def register(request):
    if request.method == 'POST':
        form = ModuleRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system #################################### 
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ################################################################## 
            messages.success(request, f'You have just registered for a module')
            return redirect('welcome')
    else:
        form = ModuleRegistrationForm()
    return render(request, 'management/registration.html', {'form': form, 'title':'Module Registration Form'})



class ModuleRegisterationForm(request):
    class Meta:
        model = Module
        fields = ['registered_students']
        
        if 'subscribe' in request.POST:
            User = request.POST.get("user")
            User.save()
            messages.info(request, 'You have successfully registered for {{Module.name}}')

        if 'unsubscribe' in request.POST:
            Module.objects.get(
            User = request.POST.get("user")).delete()
            messages.info(request, 'You are no longer registered for  {{Module.name}}')

        return render(request, 'welcome.html')
"""