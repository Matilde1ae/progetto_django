from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
    ('Informazioni', {'fields': ('numero_telefono', 'role')}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
