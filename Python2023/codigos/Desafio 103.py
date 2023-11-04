# Desafio 103 Faça um programa que tenha uma função chamada ficha(), que
# receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.

def ficha(nome=0,gols=0):
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

print(ficha(nome,Gols))
