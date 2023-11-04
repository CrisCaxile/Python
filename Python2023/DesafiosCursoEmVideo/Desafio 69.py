# Desafio 69 Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# A) Quantas pesssoas tem mais de 18 anos
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos

print('-'*50)
print('PROGRAMA DE ANÁLISE DE CADASTRAMENTO')
print('-'*50)

PessoasMais18 = 0
HomensCadastrados = 0
MulheresMenosDe20Anos = 0

while True:

    idade = input('Digite a idade de uma pessoa: ')
    idadeNumero = int(idade)

    if idadeNumero > 18:
        PessoasMais18 += 1

    while idade.isdigit() == False or idadeNumero > 122:
        idade = input('Digite a idade de uma pessoa: ')
        idadeNumero = int(idade)

    sexo = input('Escolha entre Masculino[M] ou Feminino[F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Escolha entre Masculino[M] ou Feminino[F]: ').upper()

    if sexo == 'M':
        HomensCadastrados += 1

    if sexo == 'F' and idadeNumero < 20:
        MulheresMenosDe20Anos += 1

    pergunta = input('Você deseja continuar o programa? [S] para Sim ou [N] para Não: ').upper()
    if pergunta == 'N':
        break

print('Há',PessoasMais18,'pessoas maior de 18 anos.')
print('Foram cadastrados',HomensCadastrados,'homens !')
print('Têm',MulheresMenosDe20Anos,'mulheres com menos de 20 anos')
print('---------FIM------------')
