from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações de Tipo', {'fields': ('tipo_usuario',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações de Tipo', {'fields': ('tipo_usuario',)}),
    )
    list_display = ['username', 'email', 'tipo_usuario', 'is_staff']
    list_filter = ['tipo_usuario', 'is_staff', 'is_superuser']
