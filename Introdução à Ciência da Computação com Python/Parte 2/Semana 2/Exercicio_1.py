"""
Escreva uma função maiuscula que recebe uma frase como parâmetro e devolve e devolve uma string com as letras maiusculas
"""

def maiusculas (frase):

    num_caracteres = len (frase)

    maiusculas = ""

    for i in range (num_caracteres):

        letra = frase [i]

        if ord (letra) >= 65 and ord (letra) <= 90:
            maiusculas += letra

    return maiusculas

#   #   #
##  ##  ##
### ### ###