# Desafio 54. Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pesoas ainda não atingiram a maioridade
# e quantas já são maiores

maiorI = 0
menorI = 0
for ano in range(0,7):
    x = int(input('Digite o ano de nascimento de sete pessoas: '))
    if x <= 2005:
        maiorI += 1
    else:
        menorI += 1
print('\033[35mTem',maiorI,'pessoas maior de idade e ',menorI,' pessoas de menor !\033[m')
