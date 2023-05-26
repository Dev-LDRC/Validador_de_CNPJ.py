def gerador_cnpj():
    import random

    # GERANDO OS NUMEROS
    gerador = ''
    for x in range(1,12):
        nx = random.randint(0,9)
        gerador += str(nx)

    # CONSTRUÇÃO DA ESTRUTURA DE CNPJ
    cnpj = ''
    for n in gerador:
        if len(cnpj) in [2, 6]:
            cnpj += '.'
            cnpj += n
        elif len(cnpj) == 10:
            cnpj += '/0001'
            cnpj += '-'
        else:
            cnpj += n

    return cnpj