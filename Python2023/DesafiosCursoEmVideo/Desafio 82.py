# Desafio 82 Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

print('='*50)
print('\033[36m PROGRAMA DE LISTAS \033[m')
print('='*50)

lista = []
listaPar = []
listaImpar = []
pergunta = 'S'

while pergunta.upper() == 'S':
    x = int(input('Digite um valor: '))
    lista.append(x)

    if x % 2 == 0:
        listaPar.append(x)
    else:
        listaImpar.append(x)

    pergunta = input('Você deseja continuar? [S] [N]: ')

    while pergunta.upper() not in 'SN':
        print('Você não digitou corretamente.')
        print('Tente novamente !')
        pergunta = input('Você deseja continuar? [S] [N]: ')

print('='*50)
print(lista)
print('Os valores pares digitados dentro da lista são:',listaPar)
print('Os valores ímpares digitados dentro da lista são:',listaImpar)
