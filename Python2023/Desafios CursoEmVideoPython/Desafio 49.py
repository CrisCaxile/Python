# Desafio 49. Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

print('\033[34m.............DESAFIO DA TABUADA...........\033[m')
usuario = int(input('Escolha um número:'))

for tabuada in range(1,11):
    print(usuario,'x',tabuada,'=',usuario*tabuada )
