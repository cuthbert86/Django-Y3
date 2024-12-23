from . import views
from users.views import profile, register
from django.urls import path
from .views import (PostListView,
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView,)
# from rest_framework import routers

app_name = 'itreporting'


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('policies', views.policies, name='policies'),
    path('regulations', views.regulations, name='regulations'),
    path('contact', views.contact, name='contact'),
    path('report/', views.report, name='report'),
    path('reportlist/', PostListView.as_view(), name='reportlist'),
    path('issues/<int:pk>', PostDetailView.as_view(), name='issue-detail'),
    path('issue/new', PostCreateView.as_view(), name='issue-create'),
    path('issues/<int:pk>/update/', PostUpdateView.as_view(),
         name='issue-update'),
    path('issue/<int:pk>/delete/', PostDeleteView.as_view(),
         name='issue-delete'),
    path('itreporting/send_mail1', views.send_mail1, name='email'),

]
