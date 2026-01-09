# ============================================
# Projeto: Gerenciador de Biblioteca
# Arquivo: main.py
# ============================================
# Este módulo implementa as classes principais:
# - Livro: representa um livro com título, autor, ano e status.
# - Biblioteca: gerencia a coleção de livros e suas operações.
# ============================================

# Classe que representa um livro
class Livro:
    def __init__(self, titulo, autor, ano):
        # Atributos básicos do livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        # Status inicial: todo livro começa como disponível
        self.status = "disponível"

    def __str__(self):
        # Retorna uma string formatada com as informações do livro
        return f"{self.titulo} ({self.ano}) - {self.autor} [{self.status}]"


# Classe que representa a biblioteca
class Biblioteca:
    def __init__(self):
        # Lista que armazena todos os livros cadastrados
        self.livros = []

    def adicionar_livro(self, livro):
        # Adiciona um objeto Livro à lista de livros
        self.livros.append(livro)

    def listar_livros(self):
        # Imprime todos os livros cadastrados na biblioteca
        for livro in self.livros:
            print(livro)

    def buscar_por_titulo(self, termo):
        # Busca livros pelo título (ignora maiúsculas/minúsculas)
        termo = termo.lower()
        return [livro for livro in self.livros if termo in livro.titulo.lower()]

    def emprestar_livro(self, titulo):
        # Marca um livro como emprestado, se estiver disponível
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.status == "disponível":
                    livro.status = "emprestado"
                    return True  # Empréstimo realizado com sucesso
                else:
                    return False  # Livro já estava emprestado
        return None  # Livro não encontrado

    def devolver_livro(self, titulo):
        # Marca um livro como disponível novamente, se estava emprestado
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.status == "emprestado":
                    livro.status = "disponível"
                    return True  # Devolução realizada com sucesso
                else:
                    return False  # Livro não estava emprestado
        return None  # Livro não encontrado


# ============================================
# Exemplo de uso (pode ser removido em produção)
# ============================================
if __name__ == "__main__":
    # Criando biblioteca
    bib = Biblioteca()

    # Criando livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)

    # Adicionando livros
    bib.adicionar_livro(livro1)
    bib.adicionar_livro(livro2)

    # Listando livros
    print(" Lista de livros:")
    bib.listar_livros()

    # Buscando por título
    print("\n Busca por 'Dom':")
    resultado = bib.buscar_por_titulo("Dom")
    for livro in resultado:
        print(livro)

    # Empréstimo e devolução
    print("\n Empréstimo de 'Dom Casmurro':")
    bib.emprestar_livro("Dom Casmurro")
    bib.listar_livros()

    print("\n Devolução de 'Dom Casmurro':")
    bib.devolver_livro("Dom Casmurro")
    bib.listar_livros()