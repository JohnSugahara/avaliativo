import sys
from query import Database
from teacher_crud import TeacherCRUD

class CLI:
    def __init__(self):
        uri = "bolt://localhost:7687"  # Altere conforme necessário
        user = "neo4j"
        password = "password"  # Substitua pela senha do banco de dados
        self.db = Database(uri, user, password)
        self.teacher_crud = TeacherCRUD(self.db)

    def questoes(self):
        # Questão 1
        print("Questão 01:")
        results_q1 = self.db.questao_01()
        for key, result in results_q1.items():
            print(f"{key}: {result}")

        # Questão 2
        print("\nQuestão 02:")
        results_q2 = self.db.questao_02()
        for key, result in results_q2.items():
            print(f"{key}: {result}")

    def executar_crud(self):
        # Criando 'Chris Lima'
        self.teacher_crud.create("Chris Lima", 1956, "189.052.396-66")
        print("\nProfessor 'Chris Lima' criado com sucesso.")

        # Pesquisando 'Chris Lima'
        chris = self.teacher_crud.read("Chris Lima")
        print("\nProfessor encontrado:", chris)

        # Atualizando CPF de 'Chris Lima'
        self.teacher_crud.update("Chris Lima", "162.052.777-77")
        print("\nCPF de 'Chris Lima' atualizado com sucesso.")

    def run(self):
        print("Bem-vindo ao CLI!")
        while True:
            print("\n1 - Executar Questões 1 e 2")
            print("2 - Executar CRUD para 'Chris Lima'")
            print("3 - Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.questoes()
            elif choice == "2":
                self.executar_crud()
            elif choice == "3":
                self.db.close()
                print("Saindo do programa.")
                sys.exit()
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
