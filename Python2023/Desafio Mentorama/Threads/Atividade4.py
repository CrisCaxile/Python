import threading,time

TI = time.time()
valor = 0

while valor <= 1000:
    print(valor)
    valor+=1

TF = time.time()
Result = TF-TI
print(f'O tempo de execução sem threads foi de {Result}')

def funcaoThread(valor):
    ti = time.time()
    for v in range(valor):
        print(v)
    tf = time.time()
    result = tf-ti
    print(f'O tempo que resultou com threads foi de {result}')

t1 = threading.Thread(target=funcaoThread,args=(1001,)).start()

