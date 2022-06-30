Velocidade = int(input("Informe a sua velocidade: "))
m = Velocidade - 80
Multa = 7.00 * m         
if Velocidade <= 80:
    print("Você não foi multado!")
if Velocidade > 80:
    print(f"Você foi multado em {Multa:.2f} R$")
