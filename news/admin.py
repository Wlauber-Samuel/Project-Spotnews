from django.contrib import admin
from .models import Category, News, User

# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(News)
