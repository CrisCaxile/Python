#Exercicio 06

class ContaCorrente:
    def __init__(self,NumeroDaConta,NomeCorrentista,Saldo):
        self.NumeroDaConta = NumeroDaConta
        self.NomeCorrentista = NomeCorrentista
        self.Saldo = Saldo

    def AlterarNome(self,A):
        self.NomeCorrentista = A
        print("Você alterou o nome do correntista para ",A)

    def Deposito(self):
        print("Você depositou na conta um valor de ",deposito," R$")

    def Saque(self):
        if self.Saldo < saque:
            print("Você está tentando sacar um valor que não possui em saldo.")
        else:
            print("Você fez um saque de ",saque," R$ , agora a sua conta possui ",self.Saldo-saque, "R$")

nome = input("Digite o nome do correntista: ")
deposito = int(input("Informe quanto deseja depositar na sua conta: "))
saque = int(input("Informe quanto deseja sacar na sua conta: "))
Conta = ContaCorrente(223424464,nome,deposito)
Conta.Deposito()
Conta.Saque()