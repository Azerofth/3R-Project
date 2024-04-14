from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_description', 'post_image', 'post_tags', 'post_author')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('tags_name','tags_description')