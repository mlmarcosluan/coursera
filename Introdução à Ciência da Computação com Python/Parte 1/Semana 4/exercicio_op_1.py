"""
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo
"""

def main ():

    numero = int (input ("Digite um número inteiro: "))

    passagens = 0
    n = 1
    divisivel = 0
    while n <= numero and divisivel < 3:
        if numero % n == 0:
            divisivel = divisivel + 1
        n = n + 1

    if divisivel < 3:
        print ("primo")
    else:
        print ("não primo")
main ()

#   #   #
##  ##  ##
### ### ###