# teste

import numpy

lista = [[1,2,3],[2,1,2]]
#print(type(lista),lista)

array = numpy.array([[1,2,3,4,5],[3,4,5,3,4],[2,3,4,5,3]])
print(type(array))
print(array)

print(numpy.shape(array))
print(numpy.ndim(array))
print(numpy.eye(3))
print(numpy.zeros([3,2]))
print(numpy.ones([2,4]))
print(numpy.linspace(0,20,20))
print(numpy.random.rand(2)*10)
print(numpy.random.rand(3,2))
print(numpy.random.randint(0,20,5))
print(numpy.arange(0,20,3))
print(numpy.arange(1,11).reshape(2,5))
matriz1= numpy.arange(1,11).reshape(2,5)
matriz2 = numpy.arange(11,21).reshape(2,5)
print(matriz1)
print(matriz2)
soma = numpy.add(matriz1,matriz2)
print(soma)
subtracao = numpy.subtract(matriz2,matriz1)
print(subtracao)
multiplicacao = numpy.multiply(matriz1,matriz2)
divisao = numpy.divide(matriz2,matriz1)
raiz= numpy.sqrt(matriz1)
log = numpy.log(matriz2)
log2 = numpy.log2(matriz1)
print(multiplicacao)
print(divisao)
print(raiz)
print(log)
print(log2)
sen = numpy.sin(matriz1)
print(sen)