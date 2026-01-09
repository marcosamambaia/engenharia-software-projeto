# src/main.py

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.autor}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(livro)

    def buscar_por_titulo(self, titulo):
        return [livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]


if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Exemplo inicial
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    print("📚 Livros na biblioteca:")
    biblioteca.listar_livros()

    print("\n🔎 Busca por 'hobbit':")
    resultados = biblioteca.buscar_por_titulo("hobbit")
    for r in resultados:
        print(r)