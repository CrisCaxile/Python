#Crie um programa que escreva "Olá, Mundo!" na tela.

print("\033[35mOlá, Mundo!")

msg = "\033[33mOlá, Mundo!"
print(msg)

print('O tipo primitivo é: ',cores['azul'],type(programa),cores['limpar'])
print('O que você digitou é número?',cores['roxo'], programa.isnumeric(),cores['limpar'])
print('O que você digitou é letra?',cores['amarelo'], programa.isalpha(),cores['limpar'])
print('O que você digitou é espaço?',cores['azul'], programa.isspace(),cores['limpar'])
print('O que você digitou é letra maiúscula?',cores['amarelo'], programa.isupper(),cores['limpar'])
print('O que você digitou é letra minúscula?',cores['roxo'], programa.islower(),cores['limpar'])
print('O que você digitou é letra e número?',cores['azul'], programa.isalnum(),cores['limpar'])
print('O que você digitou tem primeira letra maiúscula?',cores['roxo'], programa.istitle(),cores['limpar'])
print('O que você digitou são digitos?',cores['amarelo'], programa.isdigit(),cores['limpar'])
print('O que você digitou é printavel? ',cores['azul'],programa.isprintable())
