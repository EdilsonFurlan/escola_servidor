from django.db import models
from escolas.models import Escola
from usuarios.models import Usuario

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class PaiAluno(models.Model):
    pai = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'pai'})
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="pais")

    class Meta:
        unique_together = ('pai', 'aluno')

    def __str__(self):
        return f"{self.pai.username} - {self.aluno.nome}"
