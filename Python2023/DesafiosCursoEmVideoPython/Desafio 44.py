# Desafio 44 Elabore um programa que calcule o valor a ser pago
# Por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do seu produto: '))
condicao = int(input('\033[33m Digite a sua condição de pagamento:\033[m\n'
                 '1 - À vista dinheiro/cheque\n'
                 '2 - À vista no cartão \n'
                 '3 - Em até 2x no cartão\n'
                 '4 - 3x ou mais no cartão'))
if condicao == 1:
    preco = preco - ((preco * 10) / 100)
    print('O valor do seu produto será:',preco)
elif condicao == 2:
    preco = preco - ((preco*5) / 100)
    print('O valor do seu produto será:',preco)
elif condicao == 3:
    print('O valor do seu produto será em 2 vezes de:',round(preco/2,3))
elif condicao == 4:
    preco = preco + ((preco * 20) / 100)
    print('O valor do seu produto será em 3 vezes de:',round(preco/3,3))
