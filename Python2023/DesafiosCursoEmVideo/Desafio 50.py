# Desafio 50. Desenvolva um programa que leia seis números inteiros e
# Mostre a soma apenas daqueles que forem pares. Se o valor digitado
# For ímpar, desconsidere-o.

somaNumeroPar = 0
for contagem in range(0,6):
    usuario = int(input('Digite 6 números inteiros: '))
    if usuario % 2 == 0:
        somaNumeroPar += usuario
print('A soma dos números pares são:',somaNumeroPar)