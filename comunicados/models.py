from django.db import models
from usuarios.models import Usuario
from escolas.models import Escola

class Comunicado(models.Model):
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.escola.nome})"
