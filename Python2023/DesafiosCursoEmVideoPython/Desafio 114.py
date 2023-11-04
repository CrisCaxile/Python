# Crie um código em Python que teste se o site Pudim está acessível pelo
# computador usado.

import requests

try:
    resposta = requests.get('http://www.pudim.com.br')
    resposta.status_code == 200
    print('\033[33m O site pudim está funcionando normalmente.')

except (requests.ConnectionError):
    print('\033[31m O site pudim não está funcionando.')





