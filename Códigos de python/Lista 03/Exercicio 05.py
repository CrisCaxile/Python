# Exercício 5

class Carro:
    def __init__(self,cor,marca,ano):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.velocidade = 0

    def ImprimirDados(self):
        print(self.cor,self.marca,self.ano)

    def Acelerar(self):
        self.velocidade += 20
        print("Você acelerou o carro ! a velocidade está:",self.velocidade,"Km")

    def Ligar(self):
        print("Você ligou o carro !!")

    def desligar(self):
        print("Você desligou o carro.")

carro1 = Carro("Azul","Ford",2010)
carro2 = Carro("Preto","Nissan",2020)
carro3 = Carro("Cinza","Fiat",2013)

carro1.ImprimirDados()
carro2.ImprimirDados()
carro3.ImprimirDados()
print(carro2.marca)
carro3.Ligar()
carro3.Acelerar()
carro3.desligar()