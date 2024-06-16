"""
Escreva a função maior_elemento que recebe como parâmetro uma lista com númerosinteiros e 
devolve um número inteiro correspondente ao maior valor presente na lista recebida
"""

def maior_elemento (lista):

    maior = lista [0]

    for elemento in lista:

        if elemento > maior:
            maior  = elemento

    return maior

#   #   #
##  ##  ##
### ### ###