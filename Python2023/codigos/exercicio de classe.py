class Pessoa:
    def __init__(self,Nome,CPF,RG,Endereco,Telefone):
        self.Nome = Nome
        self.CPF = CPF
        self.RG = RG
        self.Endereco = Endereco
        self.Telefone = Telefone

    def alterarDados(self):

        pergunta = input('O que você deseja alterar? ')
        if pergunta.upper() == 'NOME':
            nome = input('Digite o nome: ')
            self.Nome = nome

        elif pergunta.upper() == 'CPF':
            cpf = int(input('Digite o cpf: '))
            self.CPF = cpf

        elif pergunta.upper() == 'RG':
            rg = int(input('Digite o rg: '))
            self.RG = rg

        elif pergunta.upper() == 'ENDERECO':
            endereco = input('Digite o endereco: ')
            self.Endereco = endereco

        elif pergunta.upper() == 'TELEFONE':
            telefone = int(input('Digite o telefone: '))
            self.Telefone = telefone

    def mostrarDados(self):
        print(self.Nome)
        print(self.CPF)
        print(self.RG)
        print(self.Endereco)
        print(self.Telefone)

class Funcionario(Pessoa):
    def __init__(self,Nome,CPF,RG,Endereco,Telefone,salario,cargo,dataAdmissao):
        super().__init__(Nome,CPF,RG,Endereco,Telefone)
        self.salario = salario
        self.cargo = cargo
        self.dataAdmissao = dataAdmissao

    def alterarDados(self):

        pergunta = input('O que você deseja alterar? ')
        if pergunta.upper() == 'NOME':
            nome = input('Digite o nome: ')
            self.Nome = nome

        elif pergunta.upper() == 'CPF':
            cpf = int(input('Digite o cpf: '))
            self.CPF = cpf

        elif pergunta.upper() == 'RG':
            rg = int(input('Digite o rg: '))
            self.RG = rg

        elif pergunta.upper() == 'ENDERECO':
            endereco = input('Digite o endereco: ')
            self.Endereco = endereco

        elif pergunta.upper() == 'TELEFONE':
            telefone = int(input('Digite o telefone: '))
            self.Telefone = telefone

        elif pergunta.upper() == 'SALARIO':
            salario = float(input('Digite o salario: '))
            while salario < self.salario:
                print('Tente novamente')
                salario = float(input('Digite o salario: '))

            self.salario = salario


    def mostrarDados(self):
        print(self.Nome)
        print(self.CPF)
        print(self.RG)
        print(self.Endereco)
        print(self.Telefone)
        print(self.salario)
        print(self.cargo)
        print(self.dataAdmissao)

class Cliente(Pessoa):
    def __init__(self,Nome,CPF,RG,Endereco,Telefone,conta,saldo,limite):
        super().__init__(Nome,CPF,RG,Endereco,Telefone)
        self.conta = conta
        self.saldo = saldo
        self.limite = limite

    def sacar(self):
        pergunta = float(input('Quanto você deseja sacar: '))
        while pergunta > self.saldo:
            print('ERRO, TENTE NOVAMENTE')
            pergunta = float(input('Quanto você deseja sacar: '))
        self.saldo-=pergunta

    def depositar(self):
        pergunta = float(input('Quanto voce desejar depositar: '))
        self.conta+= pergunta

    def alterarDados(self):

        pergunta = input('O que você deseja alterar? ')
        if pergunta.upper() == 'NOME':
            nome = input('Digite o nome: ')
            self.Nome = nome

        elif pergunta.upper() == 'CPF':
            cpf = int(input('Digite o cpf: '))
            self.CPF = cpf

        elif pergunta.upper() == 'RG':
            rg = int(input('Digite o rg: '))
            self.RG = rg

        elif pergunta.upper() == 'ENDERECO':
            endereco = input('Digite o endereco: ')
            self.Endereco = endereco

        elif pergunta.upper() == 'TELEFONE':
            telefone = int(input('Digite o telefone: '))
            self.Telefone = telefone

        elif pergunta.upper() == 'CONTA':
            conta = int(input('Digite sua conta: '))
            self.conta = conta

        elif pergunta.upper() == 'SALDO':

            saldo = float(input('Digite seu saldo: '))
            self.saldo = saldo
        elif pergunta.upper() == 'LIMITE':

            limite = float(input('Digite o limite: '))
            self.limite = limite

cliente1 = Cliente('Joao',0,0,'Rua',0,'BB',1000,2000)

print(cliente1.saldo)
cliente1.sacar()
print(cliente1.saldo)