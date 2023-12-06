import threading,time

def sum(primeiro,segundo):

    somatorio = 0
    while primeiro < segundo+1:
        somatorio += primeiro
        primeiro += 1
    print(somatorio)


def main():

    ti = time.time()
    lista = []
    pergunta = int(input('Digite quantas threads você deseja no programa: '))
    primeiro = float(input('Digite o PRIMEIRO intervalo de número que você deseja somar, ex = "0 a 100": '))
    segundo = float(input('Agora digite o SEGUNDO intervalor: '))
    DicionarioFracoes = {}

    somatorio = 0
    while primeiro < segundo + 1:
        somatorio += primeiro
        primeiro += 1

    for fracoes in range(1,pergunta+1):
        DicionarioFracoes[f'fracoes {fracoes}'] = fracoes
    print(somatorio)

    if pergunta == 1:
        for v in DicionarioFracoes.values():
            DicionarioFracoes[f'fracoes {v}'] = somatorio

    elif pergunta >= 2:
        contador1 = somatorio / 5
        for v in DicionarioFracoes.values():
            cont = pergunta
            contador2 = somatorio - contador1
            contador3 = contador2 - cont
            DicionarioFracoes[f'fracoes {v}'] = contador1
            contador1 = contador2
            cont /= pergunta

    print(DicionarioFracoes)
    print('\n')

    for c in range(1,pergunta+1):
        lista.append(f'thread{c}')

    for thread in lista:
        print(f'\033[33mUtilizando a \033[34m{thread}:\033[m')
        print('O somatorio de todos os números no intervalo é de: ',end='')
        thread = threading.Thread(target=sum,args=(primeiro,segundo))
        thread.start()
        thread.join()
        print('\n')
    tf = time.time()
    print(f'O tempo total do programa foi {tf-ti}')

main()