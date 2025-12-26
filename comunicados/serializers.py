from rest_framework import serializers
from .models import Comunicado
from usuarios.models import Usuario

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'tipo_usuario']

class ComunicadoSerializer(serializers.ModelSerializer):
    remetente_nome = serializers.ReadOnlyField(source='remetente.username')
    
    class Meta:
        model = Comunicado
        fields = ['id', 'remetente', 'remetente_nome', 'escola', 'titulo', 'mensagem', 'destinatarios', 'para_todos', 'criado_em']
        read_only_fields = ['remetente', 'escola', 'criado_em']
