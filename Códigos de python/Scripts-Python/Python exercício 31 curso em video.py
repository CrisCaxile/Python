from time import sleep
print("Seja bem vindo, este programa te dará um valor em R$ para a quant de km")
Distancia = float(input("Digite a distância da sua viagem em km: "))
print("Carregando..")
sleep(5)
if Distancia <= 200:
    print(f"Para a distância {Distancia} km, a passagem custa {Distancia*0.50:.2f} R$ .")    
else:
    print(f"Para a distância {Distancia} km, a passagem custa {Distancia*0.45:.2f} R$ .")
