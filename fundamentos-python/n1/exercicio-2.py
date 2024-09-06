# 29/08/24
# Arthur Meneses
# Exercício sobre Listas em Python

'''
Faça um programa que pergunte se um usuário quer inserir, apagar, ou ver os itens de uma lista.
'''
import os

opcao = None

# Função para adicionar números à lista
def adicionar(lista):
    cont = 1
    quantidade_numero = int(input('Quantos números você quer adicionar? '))
    while cont <= quantidade_numero:
        numero = int(input(f'Digite o número {cont}°: '))
        lista.append(numero)  # Adiciona o número à lista
        cont += 1

# Função para remover números da lista
def remover(lista):
    quantidade_remover = int(input('Quantos números você quer remover? '))
    
    if quantidade_remover > len(lista):
        print('Não é possível remover mais números do que há na lista.')
        return
    
    # Remove o último número da lista
    for _ in range(quantidade_remover):
        lista.pop()

# Declarando a lista
numero = []

print('Seja bem-vindo(a) ao sistema!')

while opcao != 'x' and opcao != 'X':
    os.system('cls')

    # Exibe a lista de números
    print('.' + '-'*60 + '.')
    print('|' + f'{f'{numero}': ^60}' + '|')
    print('\'' + '-'*60 + '\'')

    # Menu de opções
    print('[1] - Para adicionar')
    print('[2] - Para deletar')
    print('[X] - Sair do programa')
    opcao = input('Escolha uma opção: ')

    # Adicionar números
    if opcao == '1':
        adicionar(numero)

    # Remover números
    elif opcao == '2':
        remover(numero)

    # Sair do programa
    elif opcao == 'x' or opcao == 'X':
        print('Programa encerrado.')