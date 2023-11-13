import threading

def linha():
    print('-='*76)

def espaco():
    print(' '*45,end='')

def mensagem(frase):
    print(frase,end='')

def coluna():
    print(f'{"|"}',end=' ')

lista = ['Thread','Lock','Rlock','Condition','Event','Semaphore','BoundedSemaphore','Timer','Barrier']
RespostaDescricao = ['Thread é um comando para criação de uma thread','Lock é um comando para bloquear uma variavel compartilhada entre threads','Rlock permite apenas que uma thread chame a variavel especificada','Servem para gerenciar as threads mandando sinais se devem ser processadas','Assim como Condition servem para sinalizar threads','Tem a função de dizer quantas threads pode acessar o codigo','Atua como o semaphore dizendo o número maximo de threads a serem executadas','Serve para o programa executar em tal tempo','Atua como uma barreira dizendo a quantidade de threads necessarias para avançarem']
RespostaInicializacao = ['threading.thread(target=funcao,args=())','threading.Lock()','threading.Rlock()','threading.Condition()','threading.Event()','threading.Semaphore()','threading.BoundedSemaphore()','threading.Timer()','threading.Barrier()']
linha()
mensagem(f'\033[34m{"OBJETO":>14}'),espaco(),mensagem('DESCRIÇÃO'),espaco(),mensagem('COMANDO DE INICIALIZAÇÃO\033[m'),print('\n')
linha()

for p,v in enumerate(lista):
    print(f'{v:<20}',end=' '),print(' '*3,end=''),coluna(),print(f'{RespostaDescricao[p]:<85}',end=''),print(f'{" ":<7}',end=''),coluna(),print(RespostaInicializacao[p])
    # comando de inicialização
linha()


