# 2 - Escreva um programa para imprimir uma string "Olá, mundo!" cinco vezes,
# em que cada uma das impressões demore três segundos entre uma e outra

def tempo():
    import time
    for c in range(0,5):
        print('Olá, mundo!')
        time.sleep(3)