import random
import time
print("Vamos começar nosso mini joguinho!!!/n(^ – ^ *) / ---- ヾ (^ ω ^ *) ヾ (☆ ▽ ☆)")
print("Seja bem vindo! e vamos ver se você vai ser capaz de me vencer *-* haha")
j = int(input("Escolha um número de 0 a 5: "))
print("Carregando...")
print(".. · ヾ (>. <) シ")
tempo = time.sleep(5)
c = random.randint(0,5)
if j == c:
    print("Droga !!! você me venceu (¬_¬;)")
else:
    print("HAHAHAHA EU VENCI VOCÊ (✧ω✧)(✧ω✧)")
