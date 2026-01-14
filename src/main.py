
# Projeto: Gerenciador de Biblioteca
# Arquivo: main.py
# ============================================
# Este módulo implementa as classes principais:
# - Livro: representa um livro com título, autor, ano e status.
# - Biblioteca: gerencia a coleção de livros e suas operações.
# ============================================

# Classe que representa um livro
# Classe que representa um livro
class Livro:
    def __init__(self, titulo, autor, ano):
        # Inicializa os atributos do livro
        self.titulo = titulo  # Título do livro
        self.autor = autor    # Autor do livro
        self.ano = ano        # Ano de publicação
        self.status = "disponível"  # Status inicial do livro

    def __str__(self):
        # Retorna uma string formatada com as informações do livro
        return f"{self.titulo} ({self.ano}) - {self.autor} [{self.status}]"


# Classe que representa a biblioteca
class Biblioteca:
    def __init__(self):
        # Inicializa a lista que armazenará os livros
        self.livros = []

    def adicionar_livro(self, livro):
        # Adiciona um livro à lista da biblioteca
        self.livros.append(livro)

    def listar_livros(self):
        # Lista todos os livros cadastrados
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)

    def buscar_por_titulo(self, termo):
        # Busca livros pelo título, ignorando maiúsculas/minúsculas
        termo = termo.lower()
        resultados = [livro for livro in self.livros if termo in livro.titulo.lower()]
        if resultados:
            for livro in resultados:
                print(livro)
        else:
            print("Nenhum livro encontrado com esse título.")

    def emprestar_livro(self, titulo):
        # Empresta um livro se estiver disponível
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.status == "disponível":
                    livro.status = "emprestado"
                    print(f"Livro '{livro.titulo}' emprestado com sucesso.")
                    return
                else:
                    print("Livro já está emprestado.")
                    return
        print("Livro não encontrado.")

    def devolver_livro(self, titulo):
        # Devolve um livro se estiver emprestado
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.status == "emprestado":
                    livro.status = "disponível"
                    print(f"Livro '{livro.titulo}' devolvido com sucesso.")
                    return
                else:
                    print("Livro não está emprestado.")
                    return
        print("Livro não encontrado.")


def menu():
    # Cria uma instância da biblioteca
    biblioteca = Biblioteca()

    while True:
        # Exibe o menu de opções
        print("\n=== Gerenciador de Biblioteca ===")
        print("1. Adicionar livro")
        print("2. Listar livros cadastrados")
        print("3. Buscar livro por título")
        print("4. Emprestar livro")
        print("5. Devolver livro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Solicita dados do livro e adiciona à biblioteca
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
            print(f"Livro '{titulo}' adicionado com sucesso.")

        elif opcao == "2":
            # Lista todos os livros cadastrados
            print("\nLivros cadastrados:")
            biblioteca.listar_livros()

        elif opcao == "3":
            # Busca livros por título
            termo = input("Digite o título para busca: ")
            print(f"\nResultados da busca para '{termo}':")
            biblioteca.buscar_por_titulo(termo)

        elif opcao == "4":
            # Empresta um livro
            titulo = input("Título do livro para empréstimo: ")
            biblioteca.emprestar_livro(titulo)

        elif opcao == "5":
            # Devolve um livro
            titulo = input("Título do livro para devolução: ")
            biblioteca.devolver_livro(titulo)

        elif opcao == "6":
            # Sai do programa
            print("Saindo...")
            break

        else:
            # Opção inválida
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()