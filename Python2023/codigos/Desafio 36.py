# Desafio 36. Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor da casa
# o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

Vcasa = float(input('Digite o valor da casa: '))
Salario = float(input('Agora digite o valor do seu salário: '))
Anos = int(input('Diga em quantos anos você vai pagar: '))

porcentagem = (Salario * 30) / 100

prestacao = Vcasa / (Anos * 12)

minimo = (Vcasa / porcentagem) / 12

if prestacao > porcentagem:
    print('\033[31m O EMPRÉSTIMO FOI NEGADO !\033[m')
    print('A quantidade mínima de anos para o seu caso são:\033[31m ',round(minimo),'\033[m anos')
else:
    print('\033[34mSEU EMPRÉSTIMO FOI APROVADOO\033[m\n O valor das prestações ficará por:\033[34m',round(prestacao,3),' R$\033[m')
