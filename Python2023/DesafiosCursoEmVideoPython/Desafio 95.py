# Desafio 95 Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

print('-='*20)
print('\033[31m Cadastro Jogador de Futebol \033[m')
print('-='*20)

DadosJogador = {}
lista = []
Gols = []
somaGols = []
copia = []

while True:
    DadosJogador['Nome'] = input('Digite o nome do jogador: ')
    DadosJogador['Partidas'] = int(input('Digite quantas partidas ele jogou: '))
    Gols = []
    for v in range(0,DadosJogador['Partidas']):
        Gols.append(int(input(f'Quantos gols ele fez na partida {v+1}: ')))

    DadosJogador['Gols'] = Gols

    del DadosJogador['Partidas']
    lista.append(DadosJogador.copy())

    print('-'*40)
    pergunta = input('Você deseja continuar [S/N]: ')
    if pergunta.upper() == 'N':
        break

print('-='*30)
print(f'cod nome {"gols":>14} {"total":>22}')
print('-'*60)

for c,v in enumerate(lista):                        # pegar os gols somar dentro do for de cada dicionario e passar para a chave total de cada dict
    for d in lista[c]['Gols']:
        lista[c]['Total'] = sum(lista[c]['Gols'])


for posicao,valores in enumerate(lista):
    print(posicao,end=' ')
    for k,v in valores.items():

        hifen = '-'
        calculo1 = (4*len(valores['Nome']))
        calculo2 = (4 * len(valores['Nome'])) - ((len(valores['Nome']) - 3) * 5)
        calculo3 = 14 + ((len(valores['Gols']) - 2) *2)
        calculo4 = (14 + ((len(valores['Gols']) - 2) *2)) - ((len(valores['Gols'])-2) * 5 )
        hifen = hifen.replace('-',' ')

        if valores['Nome'] == v:
            if len(valores['Nome']) == 3:
                print(v,hifen*calculo1,end=' ')
            elif len(valores['Nome']) >= 4:
                print(v,hifen*calculo2,end=' ')



        if valores['Gols'] == v:
            if len(valores['Gols']) == 2:
                print(v,hifen*calculo3,end=' ')
            elif len(valores['Nome']) >= 3:
                print(v,hifen*calculo4,end=' ')

        if valores['Total'] == v:
            print(v)


while True:
    print('-=' * 30)
    pergunta = int(input('Mostrar dados de qual jogador? '))
    print(f'Levantamento do jogador {lista[pergunta]["Nome"]} ')
    for g,c in zip(lista[pergunta]['Gols'],range(0,len(lista))):
        print(f'Na partida {c+1},fez {g} gols.')
