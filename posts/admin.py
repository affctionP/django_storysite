from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
class userAdmin(admin.ModelAdmin):
    admin.site.register(PostModel)

class userAdmin(admin.ModelAdmin):
    admin.site.register(Comment)


# Register your models here.
