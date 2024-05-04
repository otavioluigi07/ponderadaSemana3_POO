class Animal:
    def __init__(self, nome, especie, felicidade=50):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade 

    def alimentar(self):
        self.felicidade += 10 

    def diminuir_felicidade(self):
        self.felicidade -= 5
        if self.felicidade < 0:
            self.felicidade = 0 

    def __str__(self):
        return f"{self.nome} ({self.especie}) - Felicidade: {self.felicidade}"


class Recinto:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []
        self.dinheiro = 0

    def adicionar_animal(self, animal):
        self.animais.append(animal)
        return True

    def remover_animal(self, animal):
        if animal in self.animais:
            self.animais.remove(animal)
            return True
        return False

    def listar_animais(self):
        if self.animais:
            print(f"Animais no recinto {self.nome}:")
            for animal in self.animais:
                print(animal)
        else:
            print(f"Não há animais no recinto {self.nome}.")

    def alimentar_animais(self):
        for animal in self.animais:
            animal.alimentar()
            print(f"{animal.nome} foi alimentado. Felicidade atual: {animal.felicidade}")

    def cuidar_recinto(self):
        for animal in self.animais:
            animal.diminuir_felicidade()
        print(f"Recinto {self.nome} foi cuidado. Felicidade dos animais reduzida por falta de cuidado.")

    def receber_visitantes(self, num_visitantes):
        self.dinheiro += num_visitantes * 15
        print(f"Seu recinto recebeu {num_visitantes} visitantes. Faturamento atual: {self.dinheiro} reais.")
        return self.dinheiro


# Exemplo de uso da API:
recinto_felinos = Recinto("Recinto dos Felinos")
recinto_primatas = Recinto("Recinto dos Grandes Primatas")

# Criando animais
tigre = Animal("Raj", "Tigre")
leao = Animal("Simba", "Leão")
macaco1 = Animal("Julius", "Macaco")
macaco2 = Animal("Gina", "Macaco")

# Adicionando animais aos recintos
recinto_felinos.adicionar_animal(tigre)
recinto_felinos.adicionar_animal(leao)
recinto_primatas.adicionar_animal(macaco1)
recinto_primatas.adicionar_animal(macaco2)

# Listando animais nos recintos
recinto_felinos.listar_animais()
recinto_primatas.listar_animais()

# Alimentando os animais
recinto_felinos.alimentar_animais()
recinto_primatas.alimentar_animais()

# Cuidando dos recintos
recinto_felinos.cuidar_recinto()
recinto_primatas.cuidar_recinto()

# Recebendo visitantes
recinto_felinos.receber_visitantes(50)
recinto_primatas.receber_visitantes(30)
