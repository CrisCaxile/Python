# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
# seu nome e idade em um arquivo de texto simples. O sistema só vai ter
# 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

arquivo = open('TesteEx115.txt','a+')
arquivo.close()

while True:

    print('-'*50)
    print(f'{"MENU PRINCIPAL":>31}')
    print('-'*50)

    print('\033[33m1 - \033[34mVer pessoas cadastradas')
    print('\033[33m2 - \033[34mCadastrar nova Pessoa')
    print('\033[33m3 - \033[34mSair do Sistema\033[m')
    print('-'*50)

    try:
        opcao = int(input('\033[33mSua opção: \033[m'))
        if opcao == 0 or opcao > 3:
            print('\033[31m ERRO! Valor digitado inválido\033[m')
            continue
    except:
        print('\033[31m ERRO! valor digitado inválido\033[m')
        continue

    if opcao == 1:
        print('-'*50)
        print(f'{"PESSOAS CADASTRADAS":>34}')
        print('-'*50)


        arquivo = open('TesteEx115.txt','r')
        print(arquivo.read())
        arquivo.close()

    elif opcao == 2:
        Nome = input('Nome: ')
        Idade = int(input('Idade: '))
        print(f' Novo registro de {Nome} adicionado.')
        arquivo = open('TesteEx115.txt','a')
        arquivo.write(f'\n{Nome:<15}{Idade:>24} anos')
        arquivo.close()


    elif opcao == 3:
        print('-'*50)
        print('Saindo do sistema... Até mais!')
        print('-'*50)
        break

