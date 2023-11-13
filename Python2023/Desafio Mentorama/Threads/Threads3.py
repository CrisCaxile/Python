# 3)

# a)
# O problema do produtor e consumidor é um problema de duas threads
# atuando sobre a mesma variável e que pode gerar alguns problemas
# como por exemplo uma thread que organiza e a outra que extrai os dados
# uma pode extrair mais rápido que organiza e vai gerar problemas

# Resolução: Para resolver este problema deve-se bloquear o acesso de uma
# thread enquanto a outra esta executando tal atividade se uma condição
# específica for necessária, por exemplo
# em casos de nao ter dados e a outra querer organizar.

# b)
# Existe o problema das Dead locks que são multi-threads para controlar
# o uso de um recurso que são problema de sincronização entre duas threads
# atuando para um fim específico. Por exemplo : no problema do consumidor
# e o produtor temos a troca dos controles perante a threads, porém se
# o consumidor perder o controle antes de bloquear e passar para o produtor
# teremos um problema bola de neve pois o produtor irá assumir o controle
# produzir novos dados e enviar o sinal para o consumidor, este irá ignorar
# o sinal para despertar e retomar o bloqueio que havia iniciado antes.

# Resolução: ao invés do consumir perder o controle da CPU no meio de um bloqueio
# só evitar perder o controle quando estiver totalmente bloqueado