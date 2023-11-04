# Desafio 93 Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

print('-='*20)
print('\033[31m Cadastro Jogador de Futebol \033[m')
print('-='*20)

DadosJogador = {}
Gols = []
DadosJogador['Nome'] = input('Digite o nome do jogador: ')
DadosJogador['Partidas'] = int(input('Digite quantas partidas ele jogou: '))

for v in range(0,DadosJogador['Partidas']):
    Gols.append(int(input(f'Quantos gols ele fez na partida {v+1}: ')))

DadosJogador['Gols'] = Gols

print('-='*20)
print(DadosJogador)
print('=-'*20)

for k,v in DadosJogador.items():
    print(f'{k} tem o valor {v}')
print('-='*20)

print(f'O jogador {DadosJogador["Nome"]} jogou {DadosJogador["Partidas"]} partidas.')
for g,c in zip(DadosJogador['Gols'],range(0,DadosJogador['Partidas'])):
    print(f'Na partida {c+1},fez {g} gols.')
