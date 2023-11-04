# Desafio 101 Crie um programa que tenha uma função chamada voto() que vai
# Receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto negado, opcional ou obrigatorio nas eleições

def voto(Ano):

    import datetime
    DataSistema = datetime.date.today()
    Idade = DataSistema.year - Ano

    print(f'Com {Idade} anos:',end=' ')

    if Idade < 18:
        return 'VOTO NEGADO.'

    elif Idade >= 18 and Idade < 65:
        return 'VOTO OBRIGATÓRIO.'

    else:
        return 'VOTO OPCIONAL.'


pergunta = int(input('Digite o seu ano de nascimento: '))

print(voto(pergunta))

