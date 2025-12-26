import os
import django

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from usuarios.models import Usuario
from escolas.models import Escola, ProfessorEscola
from alunos.models import Aluno, PaiAluno
from comunicados.models import Comunicado

def seed_data():
    print("Iniciando a geração de dados de teste...")

    # 1. Criar Escola
    escola, _ = Escola.objects.get_or_create(
        nome="Escola Primária Arco-Íris",
        endereco="Rua das Flores, 123"
    )
    print(f"Escola criada: {escola.nome}")

    # 2. Criar Diretor (se não existir além do admin)
    diretor, created = Usuario.objects.get_or_create(
        username="diretor1",
        email="diretor@escola.com",
        tipo_usuario="diretor"
    )
    if created:
        diretor.set_password("diretor123")
        diretor.save()
    print(f"Diretor criado: {diretor.username}")

    # 3. Criar Professor
    professor, created = Usuario.objects.get_or_create(
        username="professor1",
        email="professor@escola.com",
        tipo_usuario="professor"
    )
    if created:
        professor.set_password("professor123")
        professor.save()
    
    ProfessorEscola.objects.get_or_create(
        escola=escola,
        professor=professor,
        pode_cadastrar=True,
        pode_enviar_msg=True
    )
    print(f"Professor criado e vinculado: {professor.username}")

    # 4. Criar Pai
    pai, created = Usuario.objects.get_or_create(
        username="pai1",
        email="pai@exemplo.com",
        tipo_usuario="pai"
    )
    if created:
        pai.set_password("pai123")
        pai.save()
    print(f"Pai criado: {pai.username}")

    # 5. Criar Aluno vinculado à Escola e ao Pai
    aluno, _ = Aluno.objects.get_or_create(
        nome="Joãozinho da Silva",
        escola=escola
    )
    
    PaiAluno.objects.get_or_create(
        pai=pai,
        aluno=aluno
    )
    print(f"Aluno criado e vinculado ao pai: {aluno.nome}")

    # 6. Criar Comunicado de exemplo
    Comunicado.objects.get_or_create(
        remetente=professor,
        escola=escola,
        titulo="Bem-vindos ao Ano Letivo",
        mensagem="Olá pais e alunos, as aulas começam na próxima segunda-feira. Não esqueçam os materiais!"
    )
    print("Comunicado de teste criado.")

    print("\n--- RESUMO DE LOGIN ---")
    print("ADMIN: user: admin / pass: admin123 (Criado anteriormente)")
    print("DIRETOR: user: diretor1 / pass: diretor123")
    print("PROFESSOR: user: professor1 / pass: professor123")
    print("PAI: user: pai1 / pass: pai123")
    print("------------------------")

if __name__ == "__main__":
    seed_data()
