from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    '''Allows the custom User and it's forms to be used in the Admin'''
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # fieldsets to be used
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password', 'is_staff')
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'is_staff')
        }),
    )
    list_display = ['username', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
