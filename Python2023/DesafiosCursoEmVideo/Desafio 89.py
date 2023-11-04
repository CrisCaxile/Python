#Desafio 89. Crie um programa que leia nome e duas notas de vários alunos
#e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

print('=-'*50)
print('\033[31m Boletim com listas compostas. \033[m')
print('=-'*50)

lista = [[[]],[[],[],[]]]

while True:

    lista[0][0].append(input('Nome: '))
    n1 = float(input('Nota 1: '))
    lista[1][1].append(n1)
    n2 = float(input('Nota 2: '))
    lista[1][2].append(n2)
    media = (n1+n2)/2
    lista[1][0].append(media)
    pergunta = input('Deseja continuar? [S/N] ')

    if pergunta.upper() == 'N':
        break

    while pergunta.upper() not in 'SN':
        print('Erro !')
        pergunta = input('Deseja continuar? [S/N] ')


print('=-'*50)


print('No. NOME             MÉDIA')
print('-'*30)

for c in range(0,len(lista[0][0])):
    print(c,''*2,lista[0][0][c],' '*12,lista[1][0][round(c,1)])

print('-'*30)
while True:
    perguntaNota = int(input('Mostrar notas de qual aluno? (666 interrompe): '))
    if perguntaNota == 666:
        break

    for posicao in range(0, len(lista[0][0])):
        if perguntaNota == posicao:
            print('Notas de',lista[0][0][posicao],'são: ',lista[1][1][posicao],lista[1][2][posicao])

print('FIM....')
