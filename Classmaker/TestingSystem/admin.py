from django.contrib import admin
from .models import Question, Option, FreeText, TrueFalse, Test
# Register your models here.
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(FreeText)
admin.site.register(TrueFalse)
admin.site.register(Test)