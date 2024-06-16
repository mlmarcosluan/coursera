"""
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2
como parâmentro e devolve a quantidade de números primos que existem etre 2 e n (incluindo 2)
"""

def primo (numero):

    passagem = 1
    divisor = 0
    while passagem <= numero:
        if numero % passagem == 0:
            divisor = divisor + 1
        passagem = passagem + 1

    if divisor <= 2:
        return True
    else:
        return False

def n_primos (numero):

    passagem = 2
    primos = 0

    while passagem <= numero:
        if primo (passagem):
            primos = primos + 1
        passagem = passagem + 1

    return primos

#   #   #
##  ##  ##
### ### ###