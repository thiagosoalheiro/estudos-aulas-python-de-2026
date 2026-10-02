# Criando uma classe

class Cachorro:
    def __init__(self, nome, idade):   # construtor
        self.nome = nome               # atributo
        self.idade = idade

    def latir(self):                   # método
        print(f"{self.nome} diz: Au au!")

    def fazer_aniversario(self):
        self.idade += 1


rex = Cachorro("Rex", 3)       # criando um objeto (instância)
mel = Cachorro("Mel", 5)

rex.latir()                    # Rex diz: Au au!
rex.fazer_aniversario()
print(rex.idade)               # 4
print(mel.idade)               # 5 (não mudou: são objetos separados)

# __init__ é o construtor: roda automaticamente quando você cria o objeto.
# self representa o próprio objeto.
# Ele é o primeiro parâmetro de todo método, mas você não passa ele ao chamar: rex.latir(), e não rex.latir(rex).
# Para guardar um dado no objeto, use self.nome = nome. Sem o self., a variável some quando o método termina.

# Valores padrão e __str__

class Produto:
    def __init__(self, nome, preco, estoque=0):   # estoque é opcional
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):                            # o que o print() mostra
        return f"{self.nome} - R$ {self.preco:.2f} ({self.estoque} un.)"


p = Produto("Caneta", 2.5, 100)
print(p)    # Caneta - R$ 2.50 (100 un.)

#  dentro de listas e dicionários
# Na prática, você vai guardar vários objetos juntos:

produtos = [
    Produto("Caneta", 2.5, 100),
    Produto("Caderno", 15, 40),
]

total = 0
for p in produtos:
    total += p.preco * p.estoque
print("O total é: R$", total)