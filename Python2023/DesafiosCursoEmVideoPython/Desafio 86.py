# Desafio 86 Crie um programa que crie uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta

print('='*50)
print('\033[31m Desafio 86. Matriz em Python. \033[m')
print('='*50)

lista = list()
for ma in range(0,3):
    for me in range(0,3):
        lista.append(int(input(f'Digite um valor para {ma,me}: ')))

print('='*50)
for p,v in enumerate(lista):
    if p <= 2:
        print('[',v,']',end='')
        if p == 2:
            print(end=('\n'))
    elif p == 3 or p <= 5:
        print('[',v,']',end='')
        if p == 5:
            print(end=('\n'))
    elif p == 6 or p <= 8:
        print('[',v,']',end='')

print('\n')
print('='*50)
print('FIM.........')

