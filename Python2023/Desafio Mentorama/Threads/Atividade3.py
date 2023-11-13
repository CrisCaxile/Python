import time, threading

def print_cube(valor):
    """
    Função para imprimir o cubo de um determinado valor
    """
    time.sleep(5)
    print(f'Cubo: {valor**3}')

def print_square(valor):
    """
    Função para imprimir o quadrado de um determinado valor
    """
    time.sleep(10)
    print(f'Quadrado: {valor**2}')

if __name__ == "__main__":
    t1 = threading.Thread(target=print_square,args=(10,))
    t2 = threading.Thread(target=print_cube,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Done')

print(threading.active_count(),threading.current_thread(),threading.enumerate(),threading.current_thread().getName,threading.get_ident())