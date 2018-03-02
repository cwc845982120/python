from django.contrib import admin
from . import models


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex')

admin.site.register(models.Users, UserAdmin)
