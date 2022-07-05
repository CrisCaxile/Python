class cliente:
    def __init__(self,nome,saldo):
        self.nome = nome
        self.saldo = saldo
        self.saldo1 = 0
        self.saque = 0

    def depositar(self):
        self.saldo1 += pergunta
        print("Você depositou dinheiro na conta do cliente",nome,self.saldo1,"R$")


    def sacar(self):
        self.saque += pergunta1
        if self.saque > self.saldo1:
            print("Você está tentando sacar além do que você tem disponível")
        else:
            print("Você sacou dinheiro,o saldo atual é de:", (self.saldo1-self.saque),"R$")


nome = input("Digite o seu nome: ")
pergunta = int(input("Informe quanto deseja depositar: "))
pergunta1 = int(input("Informe quanto deseja sacar "))
cliente1 = cliente(nome,0)
cliente1.depositar()
cliente1.sacar()