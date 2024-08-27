#   15/08/2024
#   Ryan A.
#   [x]  pedir o login e senha de cadastro para o usuario
#   [x]  verificar a junção do login e senha
#   [x]  se estiver certo, imprimir certo.

print('-' * 50)
print('                   Cadastro:')
print('-' * 50)


cadastro_do_login = input('Crie seu usuário: ')
cadastro_da_senha = input('Crie sua senha: ')


print('-' * 50)
print('               Cadastro Concluído.')
print('-' * 50)


login_no_banco_de_dados = input('Digite seu usuário: ')
senha_no_banco_de_dados = input('Digite sua senha: ')

if (login_no_banco_de_dados == cadastro_do_login) and (senha_no_banco_de_dados == cadastro_da_senha):
    print('')
    print('Você acabou de entrar no sistema')
else:
    print('')
    print('USUÁRIO OU SENHA INCORRETOS!')