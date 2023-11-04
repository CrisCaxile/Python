# Desafio 76 Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

print('-' * 50)
print('\033[35m              LISTAGEM DE PREÇOS \033[m')
print('-' * 50)
tupla = ('Camisa', 54, 'Pente', 25, 'Calça', 110, 'Anel', 73, 'Brinco', 27, 'Luva', 30)


for n,k in zip(tupla[0::2],tupla[1::2]):
    print(n,end='')
    if len(n) == 5:
        print('.'*38,end='')
    if len(n) == 4:
        print('.'*39,end='')
    if len(n) == 6:
        print('.'*37,end='')
    print(' R$',k)

print('-' * 50)
