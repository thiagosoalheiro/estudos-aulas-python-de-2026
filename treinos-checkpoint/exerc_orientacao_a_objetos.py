# Crie a classe Pessoa com nome e idade, e um método apresentar() que imprime "Olá, eu sou X e tenho Y anos". Crie dois objetos e chame o método.
# Crie a classe Retangulo com largura e altura, e os métodos area() e perimetro() que retornam os valores.
# Crie a classe ContaBancaria com saldo privado, depositar, sacar (sem permitir saldo negativo) e get_saldo. Teste fazendo vários depósitos e saques.
# Crie a classe Produto (nome, preco, estoque) com __str__ e um método vender(qtd) que diminui o estoque, mas avisa se não houver quantidade suficiente.
# Crie a classe Funcionario (nome, salario) e a filha Gerente, que tem também bonus e sobrescreve um método salario_total() somando o bônus. Mostre o resultado dos dois.
# (Desafio) Crie uma classe Biblioteca que guarda uma lista de livros (objetos da classe Livro com título e autor), com métodos para adicionar livro, listar todos e buscar por título.

# 1
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return f"{self.nome} diz: Sou atleta"

    def jogar(self):
        return f"{self.nome} está jogando bola agora"

    def __str__(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos. {self.falar()} e ({self.jogar()})."


p = Pessoa("Pedro", 15)
print(p)
