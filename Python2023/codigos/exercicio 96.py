# Desafio 96 Faça um programa que tenha uma função chamada área(), que receba
# um terreno retangular (largura e comprimento) e mostre a área do terreno

'''print('Controle de Terrenos')
print('-'*20)

def área(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')

largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento (m): '))
área(largura,comprimento)'''

# Desafio 97 Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptavel
# ex: escreva('Olá,mundo !')
# saída:
# ------------
# Olá, Mundo!
# ------------

'''def Escreva(argumento):
    print('~'*(len(argumento)+2))
    print(argumento)
    print('~'*(len(argumento)+2))

print('\033[34m~'*28)
print('\033[m Programa da Função Escreva()')
print('\033[34m~'*28,'\033[m')

pergunta = input('Digite uma frase para colocar na função: ')
Escreva(pergunta)'''

# Desafio 98 Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

'''from time import sleep

print('~'*30)
print('\033[32m Programa da Função Contador() \033[m')
print('~'*30)

def Contador(i,f,p):
    if p == 0:
        p = 1

    if f < 0:
        p = -p

    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')

    for x in range(i,f+1,p):
        print(x,end=' ')
        sleep(0.3)
    print('FIM!')
    print('-='*20)

print('Contagem de 1 até 10 de 1 em 1')
Contador(1,10,1)

print('Contagem de 10 até 0 de 2 em 2')
print(Contador(10,0,-2))

print('Agora é a sua vez de personalizar a contagem!')
Inicio = int(input('Inicio: '))
Fim = int(input('Fim: '))
Passo = int(input('Passo: '))

Contador(Inicio,Fim,Passo)
'''

# Desafio 99 Faça um programa que tenha uma função chamada maior(), que
# receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior

'''from time import sleep

def maior(*valor):

    MaiorValor = 0
    print('Analisando os valores passados...')
    sleep(2)

    for c in valor:
        print(c,end=' ')
        if c > MaiorValor:
            MaiorValor = c
    

    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {MaiorValor}.')
    print('-='*20)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)'''

# Desafio 100 Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá0los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores PARES sorteados pela função anterior

'''from random import sample
lista = []
def sorteia():
    lista.append(sample(range(0,9),5))
    print(f'Sorteando 5 valores da lista:',end=' ')
    for x in lista:
        for c in x:
            print(c,end=' ')
    print('PRONTO !')

def somaPar():
    soma = 0
    print(f'Somando os valores pares de :',end=' ')
    for x in lista:
        for c in x:
            print(c,end=' ')
    print('temos',end=' ')
    for c in lista:
        for x in c:
            if x % 2 == 0:
                soma += x
    print(soma)
sorteia()
somaPar()'''

# Desafio 101 Crie um programa que tenha uma função chamada voto() que vai
# Receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto negado, opcional ou obrigatorio nas eleições

'''def voto(Ano):

    import datetime
    DataSistema = datetime.date.today()
    Idade = DataSistema.year - Ano

    print(f'Com {Idade} anos:',end=' ')

    if Idade < 18:
        return 'VOTO NEGADO.'

    elif Idade >= 18 and Idade < 65:
        return 'VOTO OBRIGATÓRIO.'

    else:
        return 'VOTO OPCIONAL.'


pergunta = int(input('Digite o seu ano de nascimento: '))

print(voto(pergunta))
'''

# Desafio 102 Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

'''def fatorial(a,show = False):
    """
    Essa função calcula o fatorial de um valor.
    :parametro a: é o valor que vai inserir o fatorial.
    :parametro b: é opcional, ele vai mostrar ou não o calculo.
    :return: não retorna valores
    """
    f = 1
    if show == False:
        for c in range(a,0,-1):
            f *= c
        print('-='*20)
        print(f)

    else:
        for c in range(a,0,-1):
            print(f'{c} x',end=' ' if c > 1 else f'= {f}')
            f *= c

fatorial(7,show= True)'''

# Desafio 103 Faça um programa que tenha uma função chamada ficha(), que
# receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.

'''def ficha(nome=0,gols=0):
    """
    Função de ficha de um jogador.
    :parametro nome: opcional, deve ser inserido o nome do jogador.
    :parametro gols: opcional, deve ser inserido quantos gols o jogador marcou.
    :retorna: Sim, retorna a mensagem com o nome e os gols.
    """

    print('-='*20)

    if nome == '':
        nome = 'Desconhecido'

    if gols == '':
        gols = 0
        
    return f'O jogador {nome} fez {gols} gols no campeonato'

nome = input('Digite o nome do jogador: ')
Gols = input('Diga quantos gols o jogador fez: ')

print(ficha(nome,Gols))'''

# Desafio 104 Crie um programa que tenha a função leiaInt(), que vai
# funcionar de forma semelhante à função input() do Python, só que fazendo
# a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

'''def leiaInt(numero):

    n = input(numero)
    while n.isdigit() == False:
        print('\033[31m ERRO! Digite um número inteiro válido. \033[m')
        n = input(numero)
    return n

n = leiaInt('Digite um valor: ')
print(f'Você digitou o número {n}')'''

# Desafio 105 Faça um programa que tenha uma função notas() que pode
# receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função.

'''def notas(* notas,sit = False):
    """
    Função notas: retorna um dicionários com a análise das notas, mostrando:
    o total, Maior e menor valor, sua média e ainda vem com um parâmetro
    opcional chamado situação.

    :param notas: posição para colocar as notas dos alunos
    :param sit: parâmetro opcional para mostrar a situação do aluno se é boa,razoável ou ruim.
    :return: retorna um dicionário com toda a análise das notas.
    """

    dicionario = {}

    soma = 0
    contagem = 0
    Maior = 0
    Menor = 999
    for c in notas:
        for d in c:
            soma += d
            contagem += 1

            if d > Maior:
                Maior = d

            if d < Menor:
                Menor = d

    dicionario['Total'] = contagem
    dicionario['Maior'] = Maior
    dicionario['Menor'] = Menor
    dicionario['Média'] = round(soma/contagem,2)

    if sit == True:
        if dicionario['Média'] >= 7:
            dicionario['Situação'] = 'BOA'

        elif dicionario['Média'] >= 6 and dicionario['Média'] < 7:
            dicionario['Situação'] = 'RAZOÁVEL'

        else:
            dicionario['Situação'] = 'RUIM'

    print('=-'*30)
    return dicionario

NotasAlunos = (4.0,7.8,8.4,6,10,2.1)
print(notas(NotasAlunos,sit = True))
help(notas)'''

# Desafio 106 Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
# A palavra 'FIM', o programa se encerrará.
# OBS: Use cores.

def helpCris(parametro):
    if parametro.capitalize() == 'Fim':
        pass
    else:
        print('\033[44m-=' * 20)
        print(f'Acessando o manual do comando "{parametro}"')
        print('-=' * 20)

        print('\033[7;40m')
        return help(parametro)

while True:
    print('\033[0;42m-='*20)
    print(f'{"SISTEMA DE AJUDA PyHELP":>30}')
    print('-=' * 20)

    pergunta = input('\033[mFunção ou Biblioteca: ')
    helpCris(pergunta)

    if pergunta.upper() == 'FIM':
        print('\033[0;41m-='*5)
        print('ATÉ LOGO!')
        print('-='*5)
        break