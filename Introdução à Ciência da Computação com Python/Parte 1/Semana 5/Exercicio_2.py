"""
Escreva uma função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro
e devolve o maior número primo menor ou igual ao número passado á função
"""

def testa_primo (x):

    testes = 0
    aux = x
    while testes < 3 and aux > 0:
        
        if x % aux == 0:
            testes = testes + 1
        aux = aux - 1

    if testes < 3:
        return True
    
    else:
        return False
    
def maior_primo (n):

    saida = False

    while not saida:
        if testa_primo (n):
            return n
        else:
            n = n - 1

#   #   #
##  ##  ##
### ### ###