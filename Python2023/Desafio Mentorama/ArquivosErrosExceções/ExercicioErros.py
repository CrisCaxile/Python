# Este programa contém alguns exemplos de erros utilizando o try e except

def tipo(t,mensagem):

    '''Essa função age como um input com o int e o float de modo que o usuário digita a resposta que se quer ter
    :param t: a pergunta que se faz ao usuário se ele quer usar o tipo inteiro ou real
    :param mensagem: parâmetro que o usuario digita a mensagem
    :return: retorna o input da mensagem, tendo um if para caso o usuario digitar inteiro e um real para'''

    if str(t).upper() == 'INTEIRO':
        return int(input(mensagem))
        

    elif str(t).upper() == 'REAL':
        return float(input(mensagem))



while True:
    try:
        pergunta = input('Você deseja utilizar um número real ou inteiro: ')

        valor1 = tipo(pergunta,'Digite um valor: ')
        valor2 = tipo(pergunta,'Agora digite outro: ')
        operacao = input('Digite a operação que você deseja realizar, Ex: "Soma" : ')

        if operacao.title() == 'Soma':
            Resultado = valor1 + valor2

        elif operacao.title() == 'Subtração':
            Resultado = valor1 - valor2

        elif operacao.title() == 'Multiplicação':
            Resultado = valor1 * valor2

        elif operacao.title() == 'Divisão':
            Resultado = valor1 / valor2



        print(f'A {operacao} entre os valores {valor1} e {valor2} é: {Resultado}')
        break

    except (ValueError):
        print('\033[31mVocê precisa digitar um valor correto para a operação funcionar.\033[m')
        continue

    except (NameError):
        print('\033[31mVocê está digitando uma operação indisponível para este programa!\033[m')

    except (ZeroDivisionError):
        print('\033[31mVocê está tentando dividir um número por zero\033[m')
        continue

    except (TypeError):
        print('\033[31mVocê não digitou se o número era real ou inteiro.\033[m')

    except (KeyboardInterrupt):
        print('\033[31mVocê interrompeu o programa. \033[m')
        break


