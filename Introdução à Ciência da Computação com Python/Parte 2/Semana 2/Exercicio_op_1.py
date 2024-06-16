"""
Escreva uma função conta_letras (frase, contar = "vogais") que recebe uma frase e devolva o numero de vogais se o 
parâmetro contar for vogais e as consoantes caso contrario
"""

def conta_letras (frase, contar = "vogais"):

    frase = frase.lower ()
    vogais = 0
    consoantes = 0
    

    for letra in frase:

        if letra != " ":

            if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
                vogais += 1

            else:
                consoantes += 1
    
    if contar == "vogais":
        return vogais
    
    else:
        return consoantes
    
#   #   #
##  ##  ##
### ### ###