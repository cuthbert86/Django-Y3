"""
URL configuration for itapps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# reverse_lazy
from users import views as user_views
from itreporting import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from management import views as student_views
from itreporting.views import send_mail1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('report',  views.report, name='report'), 
    path('/', include('itreporting.urls')),
    path('contact', views.contact, name='contact'),
#    path('', include('itreporting.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', 
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
    path('users/', user_views.profile, name='users/profile'),
    path('welcome', student_views.welcome, name='management/welcome'),
    path('modulelist', student_views.ModuleListView.as_view, 
         name='management/module_list'),
    path('module_details', student_views.ModuleView.as_view,
         name='management/module_details'),
    path("admin/password_reset/", auth_views.PasswordResetView.
         as_view(extra_context={"site_header": admin.site.site_header}), 
         name="admin_password_reset",),
    path("admin/password_reset/done/", auth_views.PasswordResetDoneView.
         as_view(extra_context={"site_header": admin.site.site_header}), 
         name="password_reset_done",),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.
         as_view(extra_context={"site_header": admin.site.site_header}), 
         name="password_reset_complete"),
    path('send_mail1', views.send_mail1, name='email'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
