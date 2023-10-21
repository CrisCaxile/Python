import matplotlib.pyplot as m
valoresx = [1,2,3,4]
valoresy = [2,3,4,3]
figura = m.figure(figsize=(20,3))
figura.suptitle("Título Geral")
figura.add_subplot(131)
m.plot(valoresx,valoresy,marker="v",ls="solid",lw=3.0,color="red",label="um dado qualquer")
m.legend()
m.title("Gráfico 1")

figura.add_subplot(133)
m.scatter(valoresx,valoresy)
m.title("Gráfico 2")

figura.add_subplot(132)
m.bar(valoresx,valoresy)
m.title("Gráfico 3")
m.show()