#letra a

def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print_spam)

#letra b


def do_twice1(cidade,hora):
   print("Hoje está fazendo sol na cidade :", cidade)
   print("O horário em que o onibus passa é de:", hora)

do_twice1('Recife',14.25)