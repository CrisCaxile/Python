# Desafio 62. Melhore o desafio 61, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerra quando ele disser
# que quer mostrar 0 termos.

w = 1
while w != 0:
    inicio = int(input('Informe o primeiro termo da PA:'))
    razaoPA = int(input('Agora escolha um número para ser a razão da PA'))

    calculo = inicio+(razaoPA*10)
    while inicio < calculo:
        print(inicio)
        inicio += razaoPA
    w = int(input('Você deseja mostrar mais algum termo? 1 - Sim / 0 - Não'))
print('FIM...')
