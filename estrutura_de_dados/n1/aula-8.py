# 29/08/24
# Arthur Meneses
# Tipos de loops em Python

contador = 1

while contador <= 10:   
    print(contador)     
    contador += 1
print('Nosso loop while encerrou.\n\n')

nome = ''

while not nome:
    nome = input('Informe o seu nome: ')
    if not nome:
        print('Você não informou o seu nome. Tente novamente.')
    else:
        break
print(f'Seu nome é {nome}')