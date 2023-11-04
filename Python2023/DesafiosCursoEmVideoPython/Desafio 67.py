# Desafio 67 Faça um programa que mostre a tabuada de vários números
# um de cada vez, para cada valor digitado pelo usuário. O programa será
# imterrompido quando o número solicitado for negativo

print('Desafio da TABUADA')
while True:
    w = 1
    usuario = int(input('Digite um número: '))

    if usuario > 0:
        while w <= 10:
            print(usuario,'x',w,'=',usuario*w)
            w += 1
    else:
        break

print('FIM..........')
