from django.contrib import admin
from .models import UserModel, Profile

# Register your models here.

# admin.site.register(UserModel)
# admin.site.register(Profile)
admin.site.register([UserModel, Profile])
