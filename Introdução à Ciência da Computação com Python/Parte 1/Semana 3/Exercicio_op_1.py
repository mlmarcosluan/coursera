"""
Neste exercicio vamos receber 4 numeor inteiro representando dois pares ordedados de x e y
e calcular a distancia entre dois pontos e imprimir
longe se a distancia for maior ou igual a 10 e perto se a distancia for menor que 10
"""
import math

def main ():

    x1 = int ( input ("Digite um numero inteiro: "))
    y1 = int ( input ("Digite um numero inteiro: "))
    x2 = int ( input ("Digite um numero inteiro: "))
    y2 = int ( input ("Digite um numero inteiro: "))

    # Agora vamos calcular a distancia

    distancia = math.sqrt (((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    if distancia >= 10:
        print ("longe")
    
    else:
        print ("perto")

main ()

#   #   #
##  ##  ##
### ### ###