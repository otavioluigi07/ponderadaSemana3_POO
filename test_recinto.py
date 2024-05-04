import unittest
from main import Animal
from main import Recinto

class TestRecinto(unittest.TestCase):
    def setUp(self):
        self.recinto = Recinto("Recinto Teste")

    def test_criar_recinto(self):
        self.assertEqual(self.recinto.nome, "Recinto Teste")
        self.assertEqual(self.recinto.animais, [])

    def test_adicionar_animal(self):
        tigre = Animal("Raj", "Tigre")
        leao = Animal("Simba", "Leão")
        self.assertTrue(self.recinto.adicionar_animal(tigre))
        self.assertTrue(self.recinto.adicionar_animal(leao))
        self.assertEqual(len(self.recinto.animais), 2)

    def test_remover_animal(self):
        tigre = Animal("Raj", "Tigre")
        self.recinto.adicionar_animal(tigre)
        self.assertTrue(self.recinto.remover_animal(tigre))
        self.assertEqual(len(self.recinto.animais), 0)

if __name__ == "__main__":
    unittest.main()
