# 3- Adapte o programa acima para calcular o tempo de processamaento do script
# Utilize time.time() e perf_counter() para apresentar a variação do tempo
import time

import Atividade2

tempoI = time.time()
Atividade2.tempo()
tempoF = time.time()
print(f'A diferença entre os tempos é de: {tempoF-tempoI} segundos')