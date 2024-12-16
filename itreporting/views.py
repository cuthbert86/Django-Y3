from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
import requests
from django.core.mail import send_mail
from itapps import settings

# Create your views here.
# def home(request):
#   return render(request, 'itreporting/home.html', {'title': 'Welcome'})


def home(request):
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
    weather_data.append(weather) # Add the data for the current city into our list

    return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})


def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'})


def regulations(request):
    return render(request, 'itreporting/regulations.html', {'title': 'IT Regulations'})


def policies(request):
    return render(request, 'itreporting/policies.html', {'title': 'IT Policies'})


class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination


@login_required
def report(request):
# Get all reported issues
    issues = Issue.objects.all()
# Create a context dictionary to pass to the template
    context = {'issues': issues}
# Render the report.html template with the context
    return render(request, 'itreporting/report.html', context)


class PostDetailView(DetailView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    @login_required
    def test_func(self):
        issue = self.get_object()
        return self.request.user(issue)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    @login_required
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']

    @login_required
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = '/report'

    @login_required
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author


def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "email.html", context)