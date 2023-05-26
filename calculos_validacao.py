def calculo_penutimo_num(cnpj_analize):
    algoritimo_calc = [5,4,3,2,9,8,7,6,5,4,3,2]
    mult_calc = []
    for x, y in enumerate(cnpj_analize):
        y = int(y)
        mult_calc.append(algoritimo_calc[x] * y)
    soma_calculos = sum(mult_calc)

    fomula = 11 - (soma_calculos % 11)

    if fomula <= 9:
        return f'{fomula}'
    else:
        return '0'

##############################################

def calculo_ultimo_num(cnpj_analize):
    algoritimo_calc = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    mult_calc = []
    for x, y in enumerate(cnpj_analize):
        y = int(y)
        mult_calc.append(algoritimo_calc[x] * y)
    soma_calculos = sum(mult_calc)

    fomula = 11 - (soma_calculos % 11)

    if fomula <= 9:
        return f'{fomula}'
    else:
        return '0'

##############################################

def montar_estrutura_cnpj(cnpj_analize):
    comparando = ''
    for n in cnpj_analize:
        if len(comparando) in [2,6]:
            comparando += '.'
            comparando += n
        elif len(comparando) == 10:
            comparando += '/'
            comparando += n
        elif len(comparando) == 15:
            comparando += '-'
            comparando += n
        else:
            comparando += n
    return comparando

##############################################

def so_numeros(cnpj):
    limpando_cnpj = ''
    for num in cnpj[:15]:
        if num.isdigit():
            limpando_cnpj += num
    return limpando_cnpj