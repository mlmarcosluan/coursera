"""
Escreva uma função soma_hipotenusas que receba como parâmentro um número inteiro positivo n
e devolva a soma de todos os inteireos entre 1 e n
"""

def e_hipotenusa (n):

    i = 1


    while i <= n:
        j = 1
        while j <= n:

            if (i ** 2) + (j ** 2) == (n ** 2):
                return True
            j = j + 1
        i = i + 1
    return False

def soma_hipotenusas (numero):

    passagem = 1
    soma = 0
    while passagem <= numero:

        if e_hipotenusa (passagem):
            soma = soma + passagem
        
        passagem = passagem + 1

    return soma

#   #   #
##  ##  ##
### ### ###