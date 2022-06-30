#Exercicio 10
Dívida = int(input("Qual o valor de sua dívida? "))
Juros = int(input("Qual o juros mensal da mesma? "))
Valor = int(input("E qual o valor mensal a ser pago? "))
tempo = Dívida/(Valor+Juros)
tempo2 = (Dívida+(Juros*tempo))/(Valor+Juros)
print(f"Sua dívida será paga em {round(tempo2,2)} meses.")
print(f"O total pago será de {round(Dívida+(Juros*tempo2),2)} R$.")
print(f"E o total de juros a ser pago será de {round(Juros*tempo2,2)} R$.")
