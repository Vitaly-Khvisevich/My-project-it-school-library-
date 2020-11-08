from django.contrib import admin
from .models import book, comments

# Register your models here.

admin.site.register(book)
admin.site.register(comments)
