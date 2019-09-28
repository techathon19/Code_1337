from django.contrib import admin
from django.apps import apps
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
models = apps.get_models()


class BasicUserAdmin(UserAdmin):
    list_display = ['username']
    fieldsets = UserAdmin.fieldsets + (
    (
        'Other info', {'fields': ('is_provider', 'is_consumer')}),
    )


admin.site.register(BasicUser, BasicUserAdmin)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass