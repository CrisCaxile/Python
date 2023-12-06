import threading,time,sqlite3

evento = threading.Event()
condicao = threading.Condition()
lock = threading.Lock()
lista = [(1),(),(),()]


def func1(texto,id):
    with condicao:
        condicao.wait()
        for contagem in range(1,5):
            print(texto)
            conversao = list(lista[1]) ########### TODAS AS TUPLAS DA LISTA MENOS A PRIMEIRA TUPLA NAO ESTAO INSERINDO OS DADOS, E ESTA DANDO ERRO DE TIPO
            list(lista[1]).append(texto)
        print('\n')

        time.sleep(3)
        condicao.notify(4)


def func2(id):
    while True:
        try:
            a = float(input('Digite o valor que deseja: '))
            b = float(input('Agora digite outro valor: '))
            conversao = list(lista[2])
            conversao[2].append(a)
            conversao[2].append(b)

        except ValueError:
            print('''Você digitou uma letra ao invés de um número
            Tente novamente!''')
            continue


        else:
            if a > b:
                print(f'O valor {a} é maior que o valor {b}\n')
                c = f'O valor {a} é maior que o valor {b}\n'
                conversao = list(lista[2])
                conversao[2].append(c)
            elif b > a:
                print(f'O valor {b} é maior que o valor {a}\n')
                d = f'O valor {b} é maior que o valor {a}\n'
                conversao = list(lista[2])
                conversao[2].append(d)
            elif a == b:
                print(f'Os dois valores são iguais\n')
                e =  'Os dois valores são iguais'
                conversao = list(lista[2])
                conversao[2].append(e)
        finally:
            with condicao:
                time.sleep(3)
                condicao.notify(1)



def func3():
    t1 = threading.Thread(target=func1,args=('ativando thread1',1),name='t1')
    t2 = threading.Thread(target=func2,args=(2,),name='t2')
    t4 = threading.Thread(target=func4,args=(4,),name='t4')
    t5 = threading.Thread(target=bancoDados,args=(5,),name='bancoDados')
    t1.start()
    t2.start()
    t4.start()
    t5.start()




def func4(id):

    with condicao:

        condicao.wait()
        listaPequena= (threading.current_thread(),
        threading.active_count(),
        threading.get_ident(),
        threading.current_thread().name,
        threading.enumerate(),
        threading.getprofile(),
        threading.getprofile(),
        threading.stack_size())

        conversao = list(lista[3])
        conversao[3].append(listaPequena)

        print(f'{threading.current_thread()}')
        print(f'{threading.active_count()}')
        print(f'{threading.get_ident()}')
        print(f'{threading.current_thread().name}')
        print(f'{threading.enumerate()}')
        print(f'{threading.getprofile()}')
        print(f'{threading.getprofile()}')
        print(f'{threading.stack_size()}')

        condicao.notify(5)
        print(type(lista[0]),type(lista[1]),type(lista[2]),type(lista[3]))
        print(lista)

def bancoDados(id):
    with condicao:
        condicao.wait()

        banco = sqlite3.connect('bancoThreads.db')
        sql1 = """CREATE TABLE Threads(codigo integer Primary Key not null,thread1 text, thread2 text, thread4 text)"""

        sql2 = """INSERT INTO Threads VALUES (?,?,?,?)"""


        banco.execute(sql1)
        banco.executemany(sql2,lista)
        banco.commit()
        comando = banco.execute("SELECT * FROM Threads")
        print(comando.fetchall())
        banco.close()


Time = threading.Timer(1,func3).start()
