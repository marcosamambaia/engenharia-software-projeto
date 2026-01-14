# ============================================
# Projeto: Gerenciador de Biblioteca
# Arquivo: test_main.py
# ============================================
# Este módulo contém testes automatizados para:
# - Classe Livro
# - Classe Biblioteca
# ============================================

import unittest
from src.main import Livro, Biblioteca

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        # Configuração inicial: cria uma biblioteca e adiciona um livro
        self.bib = Biblioteca()
        self.livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
        self.bib.adicionar_livro(self.livro1)

    def test_adicionar_livro(self):
        # Testa se o livro foi adicionado corretamente
        self.assertIn(self.livro1, self.bib.livros)

    def test_buscar_por_titulo(self):
        # Testa se a busca retorna o livro correto
        resultados = self.bib.buscar_por_titulo("Dom")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].titulo, "Dom Casmurro")

    def test_emprestar_livro(self):
        # Testa se o livro pode ser emprestado
        sucesso = self.bib.emprestar_livro("Dom Casmurro")
        self.assertTrue(sucesso)
        self.assertEqual(self.livro1.status, "emprestado")

    def test_devolver_livro(self):
        # Testa se o livro emprestado pode ser devolvido
        self.bib.emprestar_livro("Dom Casmurro")
        sucesso = self.bib.devolver_livro("Dom Casmurro")
        self.assertTrue(sucesso)
        self.assertEqual(self.livro1.status, "disponível")

if __name__ == "__main__":
    unittest.main()