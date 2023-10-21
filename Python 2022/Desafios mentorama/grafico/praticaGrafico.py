import matplotlib.pyplot as m
x = [1,3,4,5,6]
y = [1,3,4,5,7]

figura= m.figure(figsize=(10,5))
figura.suptitle("Título geral")
figura.add_subplot(231)

m.scatter(x,y,color="blue",label="dados")
m.xticks([0,3,4])
m.yticks([0,3,4])
m.title("Gráfico 1")
m.xlabel("Base")
m.ylabel("Altura")

figura.add_subplot(233)
m.bar(x,y,color="black")
m.title("Gráfico 2")
m.savefig("Graficos22.png")
m.show()