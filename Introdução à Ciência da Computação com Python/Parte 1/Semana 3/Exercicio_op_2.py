"""
Neste exercicio vamos calcular as raizes de uma equação de segundo grau
Como entrada vamos ter a, b, c
quando tiver uma unica raiz imprimir "a raiz desta equação é X"
quando tiver duas raizes imprimir "as raízes da equação são X e Y" e impressa de ordem crescente
quando não houver raizes imprimir "esta equação não possui raizes reais"
"""
import math
def main ():

    a = int (input ("Digite um numero para o a: "))
    b = int (input ("Digire um numero pra o b: "))
    c = int (input ("Digite um numero pra o c: "))

    delta = (b ** 2) - 4 * a * c

    if delta >= 0:
        if delta == 0:
            x1 = (- b) / (2 * a)
            print ("a raiz desta equação é", x1)
        
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            if x1 < x2:
                print ("as raízes da equação são", x1, "e", x2)

            else:
                print ("as raízes da equação são", x2, "e", x1)

    else:
        print ("esta equação não possui raízes reais")

main ()

#   #   #
##  ##  ##
### ### ###