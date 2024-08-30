# 29/08/24
# Arthur Meneses
# Exercício de IMC em Python

'''
Desenvolva um algoritmo que pergunte o nome, idade, peso (em kg) e altura (em m) de uma pessoa.
Este algoritmo deve utilizar essas informações para calcular o IMC (Índice de Massa Corpórea) desta pessoa.
Depois, faça o algoritmo apresentar no terminal o IMC da pessoa de acordo com sua categoria.
'''
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_line():
    print('.' + '-'*78 + '.')

def center_message(message, width):
    print(f"| {message.center(width)} |")

nome_do_usuario = input('Qual o seu nome? ')

print_line()
print("|" + f"Seja bem-vindo, {nome_do_usuario}! Vamos calcular o seu IMC...".center(78) + " |")
print_line()

idade = input("Informe sua idade: ")
peso = input("Informe seu peso (em kg): ")
altura = input("Informe sua altura (em metros): ")

idade = int(idade)
peso = float(peso)
altura = float(altura)

IMC = peso / (altura * altura)


limpar_tela()
input("Informações guardadas. Pressione Enter para receber o resultado...")

if IMC < 18.5:
    tipo_imc = "IMC abaixo do peso!"

elif 18.5 <= IMC <= 24.9:
    tipo_imc = "Com base na análise sobre o seu IMC, você está no peso recomendado!"

elif 25 <= IMC <= 29.9:
    tipo_imc = "Com base na análise sobre o seu IMC, você está em sobrepeso!"

elif 30 <= IMC <= 34.9:
    tipo_imc = "Com base na análise sobre o seu IMC, você está em obesidade grau 1!"

elif 35 <= IMC <= 39.9:
    tipo_imc = "Com base na análise sobre o seu IMC, você está em obesidade grau 2!"

else:
    tipo_imc = "Com base na análise sobre o seu IMC, você está em obesidade grau 3!"

print_line()
center_message(f"IMC: {IMC:.2f}", 78)
center_message(tipo_imc, 78)
print_line()