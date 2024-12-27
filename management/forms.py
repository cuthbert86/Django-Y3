from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from .models import Module, ContactSubmission, Registration
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from datetime import datetime


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
        Module = Module.objects
        fields = ['student', 'Module']

    def __init__(self, Module, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'student',
                'Module',
            ),
            Submit('submit', 'Submit', css_class='button white'),
        )

    def save(self, commit=True):
        Registration = super().save(commit=False)
        self.student = self.student
        self.module = Module.name
        if commit:
            Registration.save()

        return Registration
