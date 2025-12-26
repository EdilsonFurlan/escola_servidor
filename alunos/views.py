from rest_framework import viewsets, permissions
from .models import Aluno, PaiAluno
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlunoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo_usuario == 'pai':
            # Retorna apenas os alunos vinculados a este pai
            return Aluno.objects.filter(pais__pai=user)
        elif user.tipo_usuario in ['diretor', 'professor']:
             # Diretor/Professor podem ver alunos da sua escola (simplificado: ver todos por enquanto ou apenas da escola vinculada)
             # Melhor implementar filtro por escola depois. Por ora, retornamos todos se for staff, ou nada.
             # Vamos assumir que diretor vÃª todos alunos da sua escola (precisaria checar vinculo).
             # Para simplificar agora:
             return Aluno.objects.all()
        return Aluno.objects.none()
