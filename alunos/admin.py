from django.contrib import admin
from .models import Aluno, PaiAluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'escola', 'criado_em']
    list_filter = ['escola']
    search_fields = ['nome']

@admin.register(PaiAluno)
class PaiAlunoAdmin(admin.ModelAdmin):
    list_display = ['pai', 'aluno']
    list_filter = ['aluno__escola']
