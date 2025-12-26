from rest_framework import serializers
from .models import Aluno, PaiAluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'escola']

