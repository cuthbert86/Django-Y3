from . import views
from django.urls import path

app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
]
