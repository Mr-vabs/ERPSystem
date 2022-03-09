from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

#er your models here.

class UserModel(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'email', 'user_type']

admin.site.register(CustomUser,UserModel)

admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_Leave)