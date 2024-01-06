from django.contrib import admin
from .models import *
from .forms import *
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

@admin.register(Cmodel)
class CmodelAdmin(admin.ModelAdmin):
    list_display = ['pk','title','author','date_quest']

@admin.register(NumQuest)
class NumQuestAdmin(admin.ModelAdmin):
    list_display = ["title","author","num_quest","description"]

@admin.register(ResponseModel)
class ResponseModelAdmin(admin.ModelAdmin):
    list_display = ["pk","response_text","response_title","response_author","response_date"]

