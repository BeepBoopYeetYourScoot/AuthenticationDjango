from django.contrib import admin
from .models import Profile, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)