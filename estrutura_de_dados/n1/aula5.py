carros_desbloqueados = ['Supra', 'Corvette', 'Fusca', 'Focus']

carros_bloqueados = ['Fiorino', 'Gol', 'Uno de Escada', 'Charger']


# Lista todos os elementos
print(type(carros_desbloqueados)[0])
print(type(carros_bloqueados)[1])

# lista por índice
print(carros_bloqueados[0:3])

# Lista por intervalo
print(carros_bloqueados[0])

 Lista ao contrário
print(' ', carros_desbloqueados[-1], end=' ')
print(' ', carros_desbloqueados[-2], end=' ')
print('', carros_desbloqueados[-3], end=' ')
print(' ', carros_desbloqueados[-4], end=' ')
print(' ', carros_desbloqueados[-5], end=' ')
print(' ', carros_desbloqueados[-6], end=' ')

Adiciona um elemento no fim da lista
carros_desbloqueados.append('Camaro')
print(carros_desbloqueados)

a = ['1', '2', '3']
b = ['4', '5', '6']

# Realiza a união das listas
a.extend(b)
a.extend(carros_bloqueados)
print(a)

# Loop para interar sobre índices de -1 a -6 (inclusive) em ordem decrescente
# for i in range(-1, -7, -1):
#    print(carros_bloqueados)
