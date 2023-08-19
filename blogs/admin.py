from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','pk','slug','description','publish']
    search_fields = ['title','description']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish'

@admin.register(Edd)
class EddAdmin(admin.ModelAdmin):
    list_display = ['pk','full_name','season','phone_number','post_id']
    search_fields = ['pk','season']
