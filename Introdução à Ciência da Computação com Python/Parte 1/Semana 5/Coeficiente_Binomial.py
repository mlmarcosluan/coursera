"""
Devemos desenvolver um programa que calcula o coeficiente binomial
"""
def def_fatorial (x):
    aux = x
    fatorial = 1
    while aux > 0:
        fatorial = fatorial * aux
        aux = aux - 1
    
    return fatorial



def main ():

    n = int (input ("Digite um numero inteiro para o número n: "))
    k = int (input ("Digite um numero inteiro para a classe k: "))

    coeficiente = (def_fatorial (n)) / ((def_fatorial (k)) * (def_fatorial (n - k)))

    print (coeficiente)

main ()

#   #   #
##  ##  ##
### ### ###