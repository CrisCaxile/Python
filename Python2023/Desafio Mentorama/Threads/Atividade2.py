import threading,time

class MinhaThread():
    def mostraNúmeros(self):
        c = 0
        print(threading.current_thread().getName())
        time.sleep(1)
        while c <= 10:
            print(c)
            c +=1 

objeto1 = MinhaThread()

#t1 = threading.Thread(target=objeto1.mostraNúmeros()).start()

#t2 = threading.Thread(target=objeto1.mostraNúmeros()).start()

#t3 = threading.Thread(target=objeto1.mostraNúmeros()).start()
print(threading.active_count())
print(threading.get_ident())
print(threading.current_thread().getName)
print(threading.enumerate())



