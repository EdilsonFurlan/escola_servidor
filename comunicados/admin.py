from django.contrib import admin
from .models import Comunicado

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'escola', 'remetente', 'criado_em']
    list_filter = ['escola', 'criado_em']
    search_fields = ['titulo', 'mensagem']
