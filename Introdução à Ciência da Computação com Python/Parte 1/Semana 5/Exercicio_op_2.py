"""
Escreva uma função maximo que devolve o maior valor dentre tres inteiros recebido e devolva o maior deles
"""


def maximo (x, y, z):

    if x > y and x > z: # x é o maior
        return x
    
    elif y > x and y > z: # y é o maior
        return y
    
    else:
        return z

#   #   #
##  ##  ##
### ### ###