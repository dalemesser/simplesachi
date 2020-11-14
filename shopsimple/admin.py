from django.contrib import admin
from . models import Fruits


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock")


admin.site.register(Fruits,ProductAdmin)
