from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    USER_TYPES = (
        ('diretor', 'Diretor'),
        ('professor', 'Professor'),
        ('pai', 'Pai'),
    )
    tipo_usuario = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"
