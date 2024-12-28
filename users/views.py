from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile, User

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'{username} account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account.')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form, 'title': 
                                                       'Student Registration'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.Profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 
                             'Your account has been successfully updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.Profile)
        context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'}
        return render(request, 'users/profile.html', context)
