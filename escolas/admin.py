from django.contrib import admin
from .models import Escola, DocumentoEscola, ProfessorEscola

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'criado_em']
    search_fields = ['nome']

@admin.register(DocumentoEscola)
class DocumentoEscolaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'escola', 'enviado_por', 'criado_em']
    list_filter = ['escola', 'criado_em']

@admin.register(ProfessorEscola)
class ProfessorEscolaAdmin(admin.ModelAdmin):
    list_display = ['professor', 'escola', 'pode_cadastrar', 'pode_enviar_msg']
    list_filter = ['escola', 'pode_cadastrar', 'pode_enviar_msg']
