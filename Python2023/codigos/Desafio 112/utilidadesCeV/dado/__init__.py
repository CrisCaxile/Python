def leiaDinheiro(argumento):
    valor = input(argumento)
    while valor == '':
        print(f'\033[31mErro! Vazio não é um valor.\033[m')
        valor = input(argumento)
        valor = valor

    while valor.isalpha() == True:
        print(f'\033[31mErro! palavras não são permitidas.\033[m')
        valor = input(argumento)
        valor = valor

    if ',' in valor:
        valor = valor.replace(',','.')
    return valor