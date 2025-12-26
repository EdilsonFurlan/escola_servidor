from django.db import models
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Comunicado
from .serializers import ComunicadoSerializer
from usuarios.models import Usuario
from escolas.models import ProfessorEscola

class ComunicadoViewSet(viewsets.ModelViewSet):
    serializer_class = ComunicadoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo_usuario in ['diretor', 'professor']:
            # Diretores e professores veem comunicados que enviaram
            return Comunicado.objects.filter(remetente=user).order_by('-criado_em')
        elif user.tipo_usuario == 'pai':
            # Pais veem comunicados direcionados a eles ou para todos na escola
            return Comunicado.objects.filter(
                models.Q(destinatarios=user) | models.Q(para_todos=True)
            ).distinct().order_by('-criado_em')
        return Comunicado.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        # Busca a escola vinculada (pode ser via ProfessorEscola)
        perf = ProfessorEscola.objects.filter(professor=user).first()
        if perf:
            serializer.save(remetente=user, escola=perf.escola)
        else:
            # Se não for professor, tenta pegar a primeira escola do sistema para teste
            # Ou o admin vincula o diretor manualmente depois.
            from escolas.models import Escola
            escola = Escola.objects.first()
            serializer.save(remetente=user, escola=escola)

class ParentsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Retorna apenas usuários do tipo 'pai'
        return Usuario.objects.filter(tipo_usuario='pai')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{"id": u.id, "username": u.username, "name": f"{u.first_name} {u.last_name}".strip() or u.username} for u in queryset]
        return Response(data)
