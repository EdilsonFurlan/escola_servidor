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

    # 2. Criar Diretores (2)
    for i in range(1, 3):
        username = f"diretor{i}"
        diretor, created = Usuario.objects.get_or_create(
            username=username,
            email=f"{username}@escola.com",
            tipo_usuario="diretor"
        )
        if created:
            diretor.set_password(f"{username}123")
            diretor.save()
        print(f"Diretor criado: {diretor.username}")

    # 3. Criar Professores (2)
    for i in range(1, 3):
        username = f"professor{i}"
        professor, created = Usuario.objects.get_or_create(
            username=username,
            email=f"{username}@escola.com",
            tipo_usuario="professor"
        )
        if created:
            professor.set_password(f"{username}123")
            professor.save()
        
        ProfessorEscola.objects.get_or_create(
            escola=escola,
            professor=professor,
            pode_cadastrar=True,
            pode_enviar_msg=True
        )
        print(f"Professor criado e vinculado: {professor.username}")

    # 4. Criar Pais e Alunos (3)
    for i in range(1, 4):
        username = f"pai{i}"
        pai, created = Usuario.objects.get_or_create(
            username=username,
            email=f"{username}@exemplo.com",
            tipo_usuario="pai"
        )
        if created:
            pai.set_password(f"{username}123")
            pai.save()
        print(f"Pai criado: {pai.username}")

        # Criar Aluno vinculado à Escola e ao Pai
        aluno, _ = Aluno.objects.get_or_create(
            nome=f"Filho do {username}",
            escola=escola
        )
        
        PaiAluno.objects.get_or_create(
            pai=pai,
            aluno=aluno
        )
        print(f"Aluno criado e vinculado ao pai: {aluno.nome}")

    # 5. Criar Comunicado de exemplo (usando o professor1)
    professor1 = Usuario.objects.get(username="professor1")
    Comunicado.objects.get_or_create(
        remetente=professor1,
        escola=escola,
        titulo="Bem-vindos ao Ano Letivo",
        mensagem="Olá pais e alunos, as aulas começam na próxima segunda-feira. Não esqueçam os materiais!"
    )
    print("Comunicado de teste criado.")

    print("\n--- RESUMO DE LOGIN ---")
    print("ADMIN: user: admin / pass: admin123 (Se ja existir)")
    print("DIRETORES: diretor1, diretor2 / pass: [user]123")
    print("PROFESSORES: professor1, professor2 / pass: [user]123")
    print("PAIS: pai1, pai2, pai3 / pass: [user]123")
    print("------------------------")

if __name__ == "__main__":
    seed_data()
