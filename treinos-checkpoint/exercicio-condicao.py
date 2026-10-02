"""Peça um número ao usuário e diga se ele é positivo, negativo ou zero.
Imprima todos os números de 1 a 50 que são múltiplos de 3.
Calcule a soma de todos os números de 1 a 100 usando for.
Peça senhas ao usuário com while até ele digitar "python123", e mostre quantas tentativas foram feitas.
(Desafio) Imprima a tabuada do 1 ao 10 (cada número multiplicado de 1 a 10)."""

# 1
numero = -3

if numero > 0:
    print("Esse numero é positivo")
elif numero == 0:
    print("Esse numero é zero")
elif numero < 0:
    print("Esse numero é negativo")

# 2
for i in range(3, 31, 3):
    print(i)

# 3
contador = 0
for i in range(1, 101):
    contador = contador + i
print(f"A soma de todos os numeros de 1 a 100 é:", contador)

# 4
tentativas_senha = 0
chute_senha = int(input("Qual seria a senha: "))
tentativas_senha += 1

while chute_senha != 7171:
    chute_senha = int(input("Errou, tente de novo: "))
    tentativas_senha += 1

print("Acertou em", tentativas_senha, "tentativas")

# 5
for i in range(1, 11):          # i = 1, depois 10
    for j in range(1, 11):     # j = 1 até 10
        print(i, "x", j, "=", i * j)
