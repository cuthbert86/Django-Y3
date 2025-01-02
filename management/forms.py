from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from .models import Module, ContactSubmission, Registration, Course
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.utils import timezone


@login_required
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'name',
                'email',
                'subject',
                'message',
            ),
            Submit('submit', 'Submit', css_class='button white'),
        )


@login_required
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['Module']  # User will select the module

    # This method is used to set the fields for user and registration_time automatically
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the current user from view
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user  # Set the logged-in user automatically
            self.instance.registration_time = timezone.now()  # Set the current time


@login_required
class ModuleForm(forms.ModelForm):
    model = Module
    fields = [
            'name',
            'Course_Code',
            'credits',
            'category',
            'Description',
            'Course',
            'available',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'name',
                'Course_Code',
                'credits',
                'category',
                'Description',
                'Course',
                'available',
            ),
            Submit('submit', 'Submit', css_class='button white'),
        )


@login_required
class CourseForm(forms.ModelForm):
    model = Course
    fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'name',
            ),
            Submit('submit', 'Submit', css_class='button white'),
        )
