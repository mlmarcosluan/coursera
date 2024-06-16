"""
Escreva a função remove_repetidos que receber como parâmetro uma lista com números inteiro,
verifica se a tal lista possui elementos repetidos e os remove
"""

def remove_repetidos (lista):
    lista.sort()

    lista_limpa = []

    for elemento in lista:

        if not elemento in lista_limpa: # O elemento não esta na lista

            lista_limpa.append (elemento)

    return lista_limpa

#   #   #
##  ##  ##
### ### ###