import threading, time, datetime


def funcao1():
    data = datetime.datetime.now()
    print(data)
    for c in range (1,11):
        print(f'{data.hour},{data.minute},{datetime.datetime.now().second} ')
        print(f"Processo1 {c}")
        time.sleep(2)
        

def funcao2():
    data = datetime.datetime.now()
    print(data)
    for x in range(1,11):
        print(f'{data.hour},{data.minute},{datetime.datetime.now().second} ')
        print(f"Processo2 {x}")
        time.sleep(1)



t1 = threading.Thread(target=funcao1)

t2 = threading.Thread(target=funcao2)

print(threading.current_thread())
print(threading.active_count())
print(threading.enumerate())
print(threading.get_ident())