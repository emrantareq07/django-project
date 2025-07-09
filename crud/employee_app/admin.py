from django.contrib import admin
from .models import member

class memberAdmin(admin.ModelAdmin):
    list_display="firstName","lastName","country"

admin.site.register(member,memberAdmin)