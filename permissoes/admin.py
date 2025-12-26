from django.contrib import admin
from .models import Permissao

@admin.register(Permissao)
class PermissaoAdmin(admin.ModelAdmin):
    list_display = ['professor', 'permissao', 'ativo']
    list_filter = ['permissao', 'ativo']
