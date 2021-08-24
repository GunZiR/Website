from django.contrib import admin
from register.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from register.forms import RegisterForm, UpdateForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = UpdateForm
    model = CustomUser
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User social media',
            {
                'fields': (
                    'line_id', 
                    'facebook', 
                    'twitter',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)