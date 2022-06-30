print("%"*50)
print("Seja bem vindo ao programa que identifica triângulos")
UsuarioA = float(input("Informe o comprimento de um lado do triângulo: "))
UsuarioB = float(input("Informe o comprimento do outro lado do triângulo: ")) 
UsuarioC = float(input("Informe o comprimento da base do triângulo: "))
if UsuarioA < UsuarioB+UsuarioC and UsuarioB < UsuarioA+UsuarioC and UsuarioC < UsuarioA+UsuarioB:
    print("De acordo com os comprimentos informados, Pode-se formar um triângulo.")
else:
    print("Infelizmente não pode se formar um triângulo com estes valores !")
