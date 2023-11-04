# Dentro do pacote utilidades CeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz
# de funcionar como a função input(), mas com uma validação de dados para
# aceitar apenas valores que sejam monetários.

from utilidadesCeV import dado,moeda

valor = dado.leiaDinheiro("Digite um valor: ")
print(f'Você digitou o número : {valor}')
moeda.resumo(float(valor),80,56)
