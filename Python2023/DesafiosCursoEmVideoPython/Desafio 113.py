# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))

        except (ValueError,TypeError):
            print('\033[31m ERRO! Digite um número inteiro válido. \033[m')
            continue

        except (KeyboardInterrupt):
            print('\033[31mSeu programa foi interrompido\033[m')
            return 0

        else:
            return n


def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))

        except (ValueError,TypeError):
            print('\033[31m ERRO! Digite um número real válido. \033[m')
            continue

        except(KeyboardInterrupt):
            print('\033[31mSeu programa foi interrompido.\033[m')
            return 0

        else:
            return n


pergunta1 = leiaInt()
pergunta2 = leiaFloat()
print(f'O número inteiro digitado foi {pergunta1}')
print(f'O número real digitado foi {pergunta2}')