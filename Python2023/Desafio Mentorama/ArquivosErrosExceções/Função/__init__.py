def verificar(ip):

    IpValido = []
    IpInvalido = []
    posicaoIpInvalido = []
    posicaoIpValido = []

    for k,v in ip.items():
        parte = str(v).split('.')
        for numero in parte:
            inteiro = int(numero)
            if inteiro < 0 or inteiro > 255:
                posicaoIpInvalido.append(k)

    for valor in posicaoIpInvalido:
        IpInvalido.append(ip[valor])

    for valor in ip:
        if valor not in posicaoIpInvalido:
            posicaoIpValido.append(valor)

    for valor in posicaoIpValido:
        IpValido.append(ip[valor])

    return f'[\033[32mENDEREÇO VÁLIDO]\033[m:\n{IpValido}\n\n[\033[31mENDEREÇO INVÁLIDO\033[m]:\n{IpInvalido}'

