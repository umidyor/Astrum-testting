from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','description','publish']
    search_fields = ['title','description']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish'