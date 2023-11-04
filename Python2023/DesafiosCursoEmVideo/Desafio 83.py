# Desafio 83. Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

lista = []
usuario = input('Digite uma expressão: ')
lista.append(usuario)


confirmacao1 = 0
confirmacao2 = 0

for x in usuario:
    if x in '(':
        confirmacao1 += 1
    if x in ')':
        confirmacao2 += 1

if confirmacao1 == confirmacao2:
    print('\033[36m A expressão está correta ! \033[m')

else:
    print('\033[31m A expressão está errada ! \033[m')

