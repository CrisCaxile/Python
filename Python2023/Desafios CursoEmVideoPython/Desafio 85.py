# Desafio 85. Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores partes e ímpares em ordem crescente

print('='*50)
print('\033[36m Desafio 85 Lista com pares e ímpares \033[m')
print('='*50)

lista = [[],[]]
for p in range(0,7):
    usuario = int(input(f'Digite o {p+1}º valor: '))

    if usuario % 2 == 0:
        lista[0].append(usuario)

    if usuario % 2 != 0:
        lista[1].append(usuario)


print('='*50)
print('Os valores pares digitados foram: ',lista[0])

print('Os valores ímpares digitados foram: ',lista[1])

print('FIM....')