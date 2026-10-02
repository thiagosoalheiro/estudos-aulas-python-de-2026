class Produto:
    def __init__(self, nome, preco, estoque=0):   # estoque é opcional
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):                            # o que o print() mostra
        return f"{self.nome} - R$ {self.preco:.2f} ({self.estoque} un.)"


p = Produto("Caneta", 2.5, 100)
print(p)    # Caneta - R$ 2.50 (100 un.)

