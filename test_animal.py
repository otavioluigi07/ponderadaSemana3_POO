import unittest
from main import Animal

class TestAnimal(unittest.TestCase):
    def test_criar_animal(self):
        animal = Animal("Raj", "Tigre")
        self.assertEqual(animal.nome, "Raj")
        self.assertEqual(animal.especie, "Tigre")
        self.assertEqual(animal.felicidade, 50)

    def test_alimentar_animal(self):
        animal = Animal("Raj", "Tigre")
        animal.alimentar()
        self.assertEqual(animal.felicidade, 60)

    def test_diminuir_felicidade(self):
        animal = Animal("Raj", "Tigre", felicidade=30)
        animal.diminuir_felicidade()
        self.assertEqual(animal.felicidade, 25)

    def test_felicidade_nao_negativa(self):
        animal = Animal("Raj", "Tigre", felicidade=2)
        animal.diminuir_felicidade()
        self.assertEqual(animal.felicidade, 0)

if __name__ == "__main__":
    unittest.main()
