# 15/08/2024
# Arthur Meneses
# Cadastro e Login em Python

# [x] pedir o login e senha de cadastro para o usuario
# [x] verificar a junção do login e senha
# [x] se estiver certo, imprimir certo.

# Limpa a tela
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 50)
print('                   Cadastro:')
print('-' * 50)


cadastro_do_login = input('Crie seu usuário: ')
cadastro_da_senha = input('Crie sua senha: ')


print('-' * 50)
print('               Cadastro Concluído.')
print('-' * 50)

os.system('cls' if os.name == 'nt' else 'clear')
input("Cadatro concluído. Pressione Enter para continuar...")

user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if (user == cadastro_do_login) and (senha == cadastro_da_senha):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Seja bem-vindo, {user}!')
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('USUÁRIO OU SENHA INCORRETOS!')