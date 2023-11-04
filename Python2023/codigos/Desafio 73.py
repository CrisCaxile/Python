# Desafio 73 Crie uma tupla preenchida com os 20 primeiros colocados da tabela
# do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da chapecoense

print('~'*50)
print('\033[36m CAMPEONATO BRASILEIRO DE FUTEBOL \033[m')
print('~'*50)
tupla = ('Botafogo','Flamengo','Palmeiras','Grêmio','Fluminense','Bragantino','Athletico-PR','São Paulo','Cuiabá','Cruzeiro','Fortaleza','Internacional','Atlético-MG','Corinthians','Santos','Goiás','Bahia','Coritiba','América-MG','Vasco da Gama')
posicao = 0

if 'Chapecoense' in tupla:
    posicao = tupla.index('Chapecoense')

print('Os 5 primeiros colocados são: ',tupla[:5])
print('Os últimos 4 colocados da tabela são: ',tupla[16:20])
print('A lista com os times em ordem alfabética são: ',sorted(tupla))
print('O time da chapecoense está na posição: ',posicao)
print('FIM...........')