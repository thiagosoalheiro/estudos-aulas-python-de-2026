# Herança
# Uma classe filha reaproveita tudo de uma classe mãe e pode acrescentar ou mudar coisas.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("...")


class Cachorro(Animal):               # Cachorro herda de Animal
    def falar(self):                  # sobrescreve o método da mãe
        print(f"{self.nome}: Au au!")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)        # super() chama o construtor da mãe
        self.cor = cor

    def falar(self):
        print(f"{self.nome}: Miau!")


animais = [Cachorro("Rex"), Gato("Mia", "preto")]
for a in animais:
    a.falar()      # cada um responde do seu jeito

