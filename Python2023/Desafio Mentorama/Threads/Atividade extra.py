import threading,time

def print_even():
    for numero in range(0,2001):
        if numero % 2 == 0:
            print(numero)

def print_odd():
    for numero in range(0,2001):
        if numero % 2 != 0:
            print(numero)

def main(Par,Impar):
    t1 = threading.Thread(target=Par)
    t2 = threading.Thread(target=Impar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

main(print_even(),print_odd())