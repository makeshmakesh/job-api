from django.contrib import admin
from .models import User, Company, Job
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(User)
admin.site.register(Company)
admin.site.register(Job)