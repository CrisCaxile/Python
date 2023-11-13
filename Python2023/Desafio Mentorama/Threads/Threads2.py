# 2)

import Threads1,threading,time

def proc2():
    """
    Imprime a mensagem processo 2 na tela
    :return: print da mensagem
    """
    print('Processo 2')

time.sleep(5)
thread1 = Threads1.t1
print('-='*20)
thread2 = threading.Thread(target=proc2())
thread2.start()
print(thread1.is_alive())
print(thread2.is_alive())
time.sleep(30)
print(thread2.is_alive())
