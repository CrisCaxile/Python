# Exercicio 02
#Vou imprimir um item da tupla.

Tupla = (1,2,3,4)
print(Tupla[3])

# Exercicio 03
#Vou imprimir o tipo de dados de cada uma das variáveis e os valores delas.

Tupla = ("Aluno","Universidade","Nota","Resultado")
w,x,y,z = Tupla
print(w,x,y,z)
print(type(w),type(x),type(y),type(z))

#Exercicio 04
#letra a
#Vou fazer a união dos 3 conjuntos

setx = set(["Apple","Mango"])
sety = set(["Mango","Orange"])
setz = set(["Mango"])

print(setx.union(sety,setz))

#Letra b
#Intercessção do setx e sety

print(setx&sety)

#Letra c
#Verifica se setx é subconjunto de sety e setz

print(setx.issubset(sety))
print(setx.issubset(setz))

#Letra d
# Verificar quais elementos do conjunto setx não existem em sety

print(setx-sety)