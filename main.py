from calculos_validacao import (calculo_penutimo_num, calculo_ultimo_num,
                                montar_estrutura_cnpj, so_numeros)
from gerador_de_cnpj_aleatorio import gerador_cnpj

#########################################################################

cnpj = gerador_cnpj()
# Se Voce quiser pode substituir o `gerador_cnpj()` e colocar em 'STRING'
# `SEU_CNPJ` com o traço e as barras CORRETAMENTE para ser analizado.

# RECOLHENDO NUMEROS PARA ANALIZAR
cnpj_em_analize = so_numeros(cnpj)

################ CALCULANDO ################

# PENULTIMO NUMERO
cnpj_em_analize += calculo_penutimo_num(cnpj_em_analize)

# ULTIMO NUMERO
cnpj_em_analize += calculo_ultimo_num(cnpj_em_analize)

################ COLOCANDO EM FORMATO DE CNPJ ################

cnpj_em_analize = montar_estrutura_cnpj(cnpj_em_analize)

################ ANALIZANDO ################

if cnpj == cnpj_em_analize:
    print('-' * 40)
    print('CNPJ valido.')
    print('\tEnviado ---->', cnpj)
    print('\tAnalizado -->', cnpj_em_analize)
    print('\tCOMPATÍVEIS')
    print('-' * 40)
else:
    print('-' * 40)
    print('CNPJ invalido.')
    print('\tEnviado ---->', cnpj)
    print('\tAnalizado -->', cnpj_em_analize)
    print('\tINCOMPATÍVEIS')
    print('-' * 40)
