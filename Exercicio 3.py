#Agenda Telefônica Python 

#Definindo Agenda
class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
#Função para adicionar contatos
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"O contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' foi adicionado com sucesso.")
#Função para remover contatos
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' foi removido com sucesso.")
        else:
            print(f"Contato '{nome}' não foi encontrado.")
#Função para pesquisar contatos
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Contato '{nome}': {self.contatos[nome]}")
        else:
            print(f"Contato '{nome}' não foi encontrado.")
#Função para listar os contatos atuais
    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"{nome}: {telefone}")
#Criando o menu interativo
def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Pesquisar contato")
        print("4. Listar contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
#Laço de repetição do menu interativo
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == "2":
            nome = input("Nome: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Nome: ")
            agenda.pesquisar_contato(nome)
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            print("Obrigado por usar a Agenda Python. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o menu
menu()