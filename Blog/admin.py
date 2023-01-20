from django.contrib import admin
from .models import Blog, Category, Author, Comment

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Author)