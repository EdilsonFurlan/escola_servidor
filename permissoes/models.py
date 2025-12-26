from django.db import models
from usuarios.models import Usuario

class Permissao(models.Model):
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'professor'})
    permissao = models.CharField(max_length=50)  # ex: nota, falta, comunicado
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('professor', 'permissao')

    def __str__(self):
        return f"{self.professor.username} - {self.permissao}"
