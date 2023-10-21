# Desafio 66 Crie um programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag)

print('~'*30)
print('\033[36m Bem vindo ao PROGRAMA 66 \033[m')
print('~'*30)
print('\033[31m Digite o número 999 se desejar parar.\033[m')

soma = 0
contagem = 0
while True:
    pergunta = int(input('Digite um número inteiro: '))

    if pergunta == 999:
        break

    soma += pergunta
    contagem += 1


print('A soma dos valores são:',soma)
print('A contagem dos valores são:',contagem)
print('\033[31m ..........FIM........... \033[m')