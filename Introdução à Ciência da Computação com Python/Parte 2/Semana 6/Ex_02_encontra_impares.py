"""
Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros e 
devolve uma outra lista apenas com os números ímpares da lista dada
"""

def encontra_impares (lista):
    ### Caso base de recursão
    if len (lista) == 0: # Lista vazia
        return []
    
    primeir_elemento = lista[0]
    sub_lista = lista[1: ]

    if primeir_elemento % 2 == 1: # O primeiro elemento é impar
        return [primeir_elemento] + encontra_impares (sub_lista)
    else: # O primeiro elemento é par
        return encontra_impares (sub_lista)

#    #    #
##   ##   ##
###  ###  ###