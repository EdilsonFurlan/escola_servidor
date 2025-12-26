from django.db import models
from usuarios.models import Usuario

class Escola(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class DocumentoEscola(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='documentos')
    enviado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  # geralmente professor ou diretor
    titulo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='documentos/')  # os arquivos vão para media/documentos/
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.escola.nome})"

class ProfessorEscola(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="professores")
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'professor'})
    pode_cadastrar = models.BooleanField(default=True)
    pode_enviar_msg = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('escola', 'professor')

    def __str__(self):
        return f"{self.professor.username} - {self.escola.nome}"
