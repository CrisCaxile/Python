from time import sleep
def linha():
    print('-'*40)

def Inicio():
    linha()
    print('MENU PRINCIPAL'.center(40))
    linha()


def Menu():
    print('\033[33m1 - \033[34mVer Pessoas Cadastradas\033[m ')
    print('\033[33m2 - \033[34mAdicionar Nova Pessoa\033[m ')
    print('\033[33m3 - \033[34mSair do Programa\033[m')
    linha()

def Funcoes():
    arquivo = open('Arquivo.txt', 'a+')
    arquivo.close()
    while True:
        try:
            Inicio()
            Menu()
            pergunta = int(input('\033[33mSua Opção: \033[m'))
            while pergunta == 0 or pergunta > 3:
                print('\033[31mValor Digitado Incorreto.')
                pergunta = int(input('\033[33mSua Opção: \033[m'))

            if pergunta == 1:
                linha()
                print('PESSOAS CADASTRADAS'.center(40))
                linha()

                arquivo = open('Arquivo.txt','r')
                print(arquivo.read())
                arquivo.close()

                linha()

            elif pergunta == 2:
                nome = input('Nome: ')
                idade = int(input('Idade: '))
                print(f'Novo Registro {nome} Cadastrado com sucesso.')
                arquivo = open('Arquivo.txt','a+')
                arquivo.write(f'{nome:<15}{idade:>24}\n')
                arquivo.close()
                linha()

            elif pergunta == 3:
                linha()
                print('Finalizando o Programa...')
                linha()
                sleep(2)
                break
        except:
            print('\033[31mVALOR DIGITADO NÃO CORRESPONDE AO MENU, TENTE NOVAMENTE !!')
            continue