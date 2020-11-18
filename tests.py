from unittest import TestCase
from calculator import comparador, multiplicacao, par_impar, soma, iterador


class TestSoma(TestCase):

    def test_soma(self):
        self.assertEqual(soma(5,7),12)
        self.assertEqual(soma(5,0),5)

class TestMultiplicacao(TestCase):

    def test_multiplicaco(self):
        self.assertEqual(multiplicacao(0, 0), 0)

class TestComparacao(TestCase):

    def test_comparacao(self):
        self.assertEqual(comparador(5,5),False)
        self.assertEqual(comparador(5,2),True)

class TestIterador(TestCase):

    def test_iterador(self):
        self.assertEqual(iterador(6), 15)

class TestParImpar(TestCase):
    def test_par_impar(self):
        self.assertEqual(par_impar(5),"ímpar")