from task.views import course
from django.contrib import admin
from django.shortcuts import redirect

from .models import courses

# Register your models here.


admin.site.register(courses)