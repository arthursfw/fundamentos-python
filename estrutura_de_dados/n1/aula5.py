# 22/08/24
# Arthur Meneses
# Listas em Python

carros_desbloqueados = ['Supra', 'Corvette', 'Fusca', 'Focus']
carros_bloqueados = ['Fiorino', 'Gol', 'Uno de Escada', 'Charger']

# Lista os tipos das listas
print(type(carros_desbloqueados))
print(type(carros_bloqueados))
print('')

# Lista por índice
print(carros_bloqueados[0:3])
print('')

# Lista por intervalo
print(carros_bloqueados[0]) # Escolhe posição da array
print('')

# Lista ao contrário
print(' ', carros_desbloqueados[-1], end=' ')
print(' ', carros_desbloqueados[-2], end=' ')
print(' ', carros_desbloqueados[-3], end=' ')
print(' ', carros_desbloqueados[-4], end=' ')
print('')

# Lista ao contrário (em forma de loop)
for i in range(-1, -5, -1):  # Ajustar para -5
    print(' ', carros_desbloqueados[i], end=' ')
print('')

# Adiciona um elemento no fim da lista
carros_desbloqueados.append('Camaro')
print(carros_desbloqueados)

a = ['1', '2', '3']
b = ['4', '5', '6']
print('')

# Realiza a união das listas
a.extend(b)
a.extend(carros_bloqueados)
print(a)

# Lista: Uma coleção (ordenada) de elementos, acessíveis por índices.