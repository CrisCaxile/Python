# Desafio 105 Faça um programa que tenha uma função notas() que pode
# receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função.

def notas(* notas,sit = False):
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
help(notas)
