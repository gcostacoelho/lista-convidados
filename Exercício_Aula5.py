numero_de_convidados = input('Quantas pessoas serão convidadas?: ')
lista_de_convidados = []
i = 0

while i < int(numero_de_convidados):
    nome_convidado = input('Qual o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append (nome_convidado)
    i += 1

print ('\nLISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print (convidado)

print ('Sera(ão)', numero_de_convidados, 'convidado(s) ao todo')

