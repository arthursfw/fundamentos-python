# 29/08/24
# Arthur Meneses
# While e While not em Python

numero = int(input('Digite um número inteiro positivo: '))

terminou = None

print(numero)

while not terminou:
    if numero % 2 == 0:
        numero = numero // 2
        print(numero)

    else:
        numero = numero * 3 + 1
        print(numero)

    if numero == 1:
        terminou = True
        break