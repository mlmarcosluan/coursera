"""
Escreva uma função primeiro_lex (lista) que recebe uma lista de strings como parâmetro e devolva o primeiro
string na ordem lexiográfica 
"""

def primeiro_lex (lista):

    primeira_palavra = lista [0]
    menor_palavra = primeira_palavra

    for palavra in lista:

        if palavra < menor_palavra:
            menor_palavra = palavra

        
    return menor_palavra

#   #   #
##  ##  ##
### ### ###