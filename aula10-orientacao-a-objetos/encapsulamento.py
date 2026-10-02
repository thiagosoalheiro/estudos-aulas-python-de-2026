# Encapsulamento
# Encapsular é proteger os dados para que só sejam alterados do jeito certo.
# Por convenção, um atributo começando com _ ou __ é "privado":

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo           # privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def get_saldo(self):               # getter
        return self.__saldo

c = Conta("Ana", 100)
c.depositar(50)
c.sacar(30)
print("Saldo final:", c.get_saldo())    # 120
# print(c.__saldo)      # dá erro: acesso direto bloqueado

# Uma forma mais elegante de fazer o getter é com @property:
#@property
#def saldo(self):
    #return self.__saldo