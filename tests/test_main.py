# tests/test_main.py
import unittest
from src.main import Livro, Biblioteca

class TestBiblioteca(unittest.TestCase):
    def test_adicionar_e_listar(self):
        biblioteca = Biblioteca()
        livro = Livro("1984", "George Orwell", 1949)
        biblioteca.adicionar_livro(livro)
        self.assertIn(livro, biblioteca.livros)

    def test_buscar_por_titulo(self):
        biblioteca = Biblioteca()
        livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
        biblioteca.adicionar_livro(livro)
        resultados = biblioteca.buscar_por_titulo("senhor")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].titulo, "O Senhor dos Anéis")

if __name__ == "__main__":
    unittest.main()