from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.User)
class CustomAdminClass(ModelAdmin):
    pass
