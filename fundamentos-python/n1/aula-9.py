# 29/08/24
# Arthur Meneses
# Empacotamento e Desempacotamento em Python

lista_de_convidados = ['Thiago', 'Silvana', 'Katarina', 'Evandro']
convidado1, convidado2, convidado3, convidado4 = lista_de_convidados

# Desse modo, cada convidado foi adicionado à variável correspondente ao seu índice, na ordem em que foram declaradas.

print(convidado1)
print(convidado4)

tupla_de_convidados = ('Marcelo', 'Guilherme', 'Zeca Robson')
print(type(tupla_de_convidados))

convidado1, *demais_convidados = ['Thiago', 'Silvana', 'Katarina', 'Evandro']
print(convidado1)
print(demais_convidados)