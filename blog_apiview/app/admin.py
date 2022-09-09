from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_superuser','is_deleted')
    readonly_fields = ('last_login', 'date_joined',)
    ordering = ('email',)
    search_fields = ('first_name', 'last_name', 'email') 
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'date_joined',
                    'last_login',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'is_deleted',
                    'user_permissions',
                    'password',
                    'role'
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)