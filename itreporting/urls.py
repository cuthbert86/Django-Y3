from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


app_name = 'itreporting'


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('report/',  views.report, name='report'),
    path('reportlist/', PostListView.as_view(), name='reportlist'),
    path('issues/<int:pk>', PostDetailView.as_view(), name='issue-detail'),
    path('issue/new', PostCreateView.as_view(), name='issue-create'),
    path('issues/<int:pk>/update/', PostUpdateView.as_view(), name='issue-update'),
    path('issue/<int:pk>/delete/', PostDeleteView.as_view(), name='issue-delete'),
]
