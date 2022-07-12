# exercicio 01

arquivo = open("Teste1.txt", "a+")
arquivo.close()
arquivo = open("Teste1.txt","w+")
arquivo.write("\033[1;35mAqui inicia o teste do arquivo de teste 1, vamos ver se funciona !\n")
arquivo.write("O arquivo funcionou completamente!\n")
arquivo.close()
arquivo = open("Teste1.txt", "r")
print(arquivo.read())
arquivo.close()