from django.contrib import admin

from blog.models import Author, Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)

# Register your models here.
