class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def mostrar_contatos(self):
        if not self.contatos:
            print("Não há contatos cadastrados.")
            return
        for i, contato in enumerate(self.contatos, start=1):
            print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email} - {'Favorito' if contato.favorito else ''}")

    def editar_contato(self, indice, nome, telefone, email):
        contato = self.contatos[indice]
        contato.nome, contato.telefone, contato.email = nome, telefone, email

    def marcar_desmarcar_favorito(self, indice):
        self.contatos[indice].favorito = not self.contatos[indice].favorito

    def mostrar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Não há contatos favoritos.")
            return
        for i, contato in enumerate(favoritos, start=1):
            print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email}")

    def apagar_contato(self, indice):
        del self.contatos[indice]

def main():
    agenda = Agenda()
    while True:
        print("\n### Menu ###")
        print("1. Adicionar contato")
        print("2. Visualizar lista de contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar contato como favorito")
        print("5. Ver lista de contatos favoritos")
        print("6. Apagar contato")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break
        elif escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contato(Contato(nome, telefone, email))
            print("Contato adicionado com sucesso!")
        elif escolha == "2":
            agenda.mostrar_contatos()
        elif escolha == "3":
            indice = int(input("Índice do contato a ser editado: ")) - 1
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            agenda.editar_contato(indice, nome, telefone, email)
            print("Contato editado com sucesso!")
        elif escolha == "4":
            indice = int(input("Índice do contato a ser marcado/desmarcado como favorito: ")) - 1
            agenda.marcar_desmarcar_favorito(indice)
            print("Contato marcado/desmarcado como favorito com sucesso!")
        elif escolha == "5":
            agenda.mostrar_favoritos()
        elif escolha == "6":
            indice = int(input("Índice do contato a ser apagado: ")) - 1
            agenda.apagar_contato(indice)
            print("Contato apagado com sucesso!")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
