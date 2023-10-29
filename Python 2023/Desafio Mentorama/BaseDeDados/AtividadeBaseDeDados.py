# CRIAÇÃO DO BANCO DE DADOS

import sqlite3 as s

banco = s.connect("BancoDeDados.db")


#sql1 = """CREATE TABLE Departamentos(Codigo Integer PRIMARY KEY NOT NULL, Nome text,Localizacao text,
 #CodigoFuncionarioGerente intenger)
#"""


#sql2 = """CREATE TABLE Funcionarios(Codigo Integer PRIMARY KEY NOT NULL,PrimeiroNome text,SegundoNome text,UltimoNome text,
#DataNasci text,CPF integer,RG integer,Endereço text,CEP integer,Cidade text,
#Fone integer,CodigoDepartamento integer,Funcao text,Salario integer)
#"""


#banco.execute(sql1)

#banco.execute(sql2)

#banco.commit()


#sql11 = """ INSERT INTO Departamentos VALUES(?,?,?,?)
#"""


#sql22 = """ INSERT INTO Funcionarios VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
#"""


#lista1 = [(1,'Logistica','Setor 1',101),(2,'Produção','Setor 2',102),(3,'Finanças','Setor 3',103)]

#lista2 = [(1,'João','Lima','Assis',2001/04/15,13494385376,3445423,'Rua Antonio viera',52034788,'Fortaleza',77934528322,1,'Assistente Logistico',2400),(2,'Maria','Leite','Silva',1996/08/23,49329023487,6483123,'Avenida corrego do alberto',43032021,'Recife',81983447398,2,'Encarregado de produção',3000),(3,'Felipe','Augusto','Bezerra',1995/09/15,84612346521,2953428,'Rua Jose Lazaro',91276100,'Fortaleza',77992436234,3,'Assistente Financeiro',2640)]

#banco.executemany(sql11,lista1)

#banco.executemany(sql22,lista2)

#banco.commit()



# A - Listar nome e sobrenome ordenado por sobrenome
# B - Listar todos os campos de funcionários ordenados por cidade
# C - Liste os funcionários que têm salário superior a R$ 1.000,00 ordenados pelo nome completo
# D - Liste a data de nascimento e o primeiro nome dos funcionários ordenados do mais novo para o mais velho
# E - Liste o total da folha de pagamento
# F - Liste o nome, o nome do departamento e a função de todos os funcionários
# G - Liste a quantidade de funcionários desta empresa
# H - Liste o nome do departamento e do funcionário ordenados por departamento e funcionário


# A
#comando = "SELECT PrimeiroNome,UltimoNome FROM Funcionarios ORDER BY UltimoNome ASC"
#printar = banco.execute(comando)
#print(printar.fetchall())

# B
#comando = "SELECT * FROM Funcionarios ORDER BY Cidade"
#printar = banco.execute(comando)
#print(printar.fetchall())

# C
#comando = "SELECT PrimeiroNome,SegundoNome,UltimoNome FROM Funcionarios WHERE Salario > 1000 ORDER BY PrimeiroNome,SegundoNome,UltimoNome"
#printar = banco.execute(comando)
#print(printar.fetchall())

# D
#sql = "SELECT PrimeiroNome,DataNasci FROM Funcionarios ORDER BY DataNasci DESC"
#printar = banco.execute(sql)
#print(printar.fetchall())

# E
#sql = "SELECT SUM(Salario) FROM Funcionarios"
#printar = banco.execute(sql)
#print(printar.fetchall())

# F
#sql = "SELECT PrimeiroNome,Nome,Funcao FROM Funcionarios,Departamentos"
#printar = banco.execute(sql)
#print(printar.fetchall())

# G
#sql = "SELECT COUNT(Codigo) FROM Funcionarios"
#printar = banco.execute(sql)
#print(printar.fetchall())

# H
#sql1 = "SELECT"
#sql = "SELECT Departamentos.Nome, Funcionarios.PrimeiroNome FROM Departamentos JOIN Funcionarios ON Departamentos.Codigo = Funcionarios.Codigo ORDER BY Departamentos.Nome,Funcionarios.Codigo"
#printar = banco.execute(sql)
#print(printar.fetchall())