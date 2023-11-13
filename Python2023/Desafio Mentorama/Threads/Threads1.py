import threading

def proc1():
    """
    Imprime a mensagem Processo 1
    :return: print na tela
    """
    print('Processo 1')

# 1)

t1 = threading.Thread(target=proc1())
t1.start()
print(t1.is_alive())
print(threading.current_thread().name)
print(threading.current_thread().ident)
print(threading.active_count())
print(threading.enumerate())




