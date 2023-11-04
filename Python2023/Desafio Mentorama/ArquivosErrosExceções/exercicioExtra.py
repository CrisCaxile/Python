import random
# oxente

class restaurante:
    import random
    def __init__(self,ItensVendidos,ValorItem,QuantItem):

        self.NumeroMesa = random.randint(1,30)
        self.ItensVendidos = [ItensVendidos]
        self.ValorItem = [ValorItem]
        self.QuantItem = QuantItem
        garcons = ['Gustavo','Felipe','Ana','Flávia','Anderson']
        self.NomeGarcom = random.choice(garcons)
        self.calculo = 0
        self.somatorio = ValorItem
        self.dia = 0


    def AdicionaItem(self):

        while True:

            Item = input('Digite o item que deseja adicionar: ')
            self.ItensVendidos.append(Item)

            Valor = int(input('Digite o valor do item(UNITARIO) que deseja adicionar: '))

            Quant = int(input('Quantidade do item: '))
            self.QuantItem += Quant
            calculo = Valor*Quant
            self.somatorio += calculo
            self.ValorItem.append(calculo)

            pergunta = input('Deseja adicionar mais itens: [S/N]: ')
            if pergunta.upper() == 'N':
                break

    def Gorjeta(self):

        self.calculo = (sum(self.ValorItem) * 10) / 100
        print(f'A gorjeta do garçom é: {self.calculo} R$')

    def FecharConta(self):

            while self.QuantItem == 0:
                print('Você não adicionou nenhum valor.')
                self.AdicionaItem()

            somatorio = sum(self.ValorItem)
            resposta = self.calculo + somatorio
            print(f'O valor da sua conta atual é: {resposta} R$')
            self.ValorItem = []
            self.ItensVendidos = []
            self.QuantItem = 0




    def FechamentoDia(self):

        resposta = self.calculo + self.somatorio
        print(f'O restaurante fechou o expediente, o faturamento do dia foi de: {resposta} R$')


    def AbreConta(self):

        print('Você abriu a conta!')
        arquivo = open('Historico de Vendas.txt','a+')
        arquivo.close()
        print(f'O número da mesa é: {self.NumeroMesa}\nO nome do garçom é: {self.NomeGarcom}')

        while True:

            print('-=' * 20)
            print(f'\033[33m{"MENU CONTA".center(35)}\033[m')
            print('-=' * 20)
            print('\033[33m1- \033[mAdicionar Item')
            print('\033[33m2- \033[mVer gorjeta')
            print('\033[33m3- \033[mMostrar conta')
            print('\033[33m4- \033[mFechamento do dia')
            print('\033[33m5- \033[mVer Histórico de venda')
            print('-=' * 20)
            pergunta = int(input('Digite qual opção você deseja: '))

            if pergunta == 1:
                self.AdicionaItem()

            elif pergunta == 2:
                self.Gorjeta()

            elif pergunta == 3:
                self.FecharConta()

            elif pergunta == 4:

                self.dia += 1
                arquivo = open('Historico de Vendas.txt', 'r')
                if arquivo.readlines() != None:
                    for valor in arquivo.readlines()[-3][5]:
                        inteiro = int(valor)
                        self.dia += inteiro
                        arquivo.close()

                arquivo.close()

                arquivo = open('Historico de Vendas.txt','a+')
                self.FechamentoDia()
                arquivo.write('-='*20)
                arquivo.write('\n')
                arquivo.write(f'Dia: {self.dia}\nO faturamento deste dia foi de: {self.calculo+self.somatorio} R$\n')
                arquivo.write('-='*20)
                arquivo.write('\n')

                arquivo.close()
                print('\033[34mPROGRAMA FINALIZADO...')
                break

            elif pergunta == 5:
                print('\033[36mHISTÓRICO DE VENDAS: \033[m')
                arquivo = open('Historico de Vendas.txt','r')
                print(arquivo.read())
                arquivo.close()

            else:
                print('\033[31mValor incorreto!\033[m')



cliente1 = restaurante('Galeto',40,1)
cliente1.AbreConta()


