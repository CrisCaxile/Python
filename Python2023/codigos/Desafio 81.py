# Desafio 81 Crie um programa que vai ler vários números e colocar em uma lista.
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
pergunta = 'S'
while pergunta.upper() == 'S':
    lista.append(int(input('Digite um valor:')))
    pergunta = input('Deseja continuar inserindo valores [S] ou [N]: ')

    while pergunta.upper() not in 'SN':
        print('Erro !')
        pergunta = input('Deseja continuar inserindo valores [S] ou [N]: ')

print('='*50)
print('A quantidade de números digitados foram:',len(lista))
lista.sort(reverse=True)
print('A lista de forma decrescente:',lista)

N5 = lista.count(5)

print('O valor 5 foi digitado ? ',end='')

if N5 >= 1:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
