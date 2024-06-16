"""
Escreva um programa que receba um número natural n na entrada e imprima n! na saida
"""

def main ():

    n = int (input ("Digite um numero natural "))
    if n == 0:
        fatorial = 1
    
    else:
        fatorial = n

    while n > 1:
        fatorial = fatorial * (n - 1)
        n = n - 1
    
    print (fatorial)
main ()

#   #   #
##  ##  ##
### ### ###