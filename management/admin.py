from django.contrib import admin
from .models import Module, ContactSubmission, Registration, Course
# Register your models here.

admin.site.register(Module)
admin.site.register(ContactSubmission)
admin.site.register(Registration)
admin.site.register(Course)
