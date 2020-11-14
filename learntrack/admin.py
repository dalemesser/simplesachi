from django.contrib import admin
from .models import Learn

class LearnAdmin(admin.ModelAdmin):
    list_display = ("date","title")
admin.site.register(Learn,LearnAdmin)
