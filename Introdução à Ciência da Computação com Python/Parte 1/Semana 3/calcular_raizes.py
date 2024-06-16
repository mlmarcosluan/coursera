"""
Esse programa tem como finalidade calcular as raizes de uma equação de segundo grau a partir
de 3 valores dados pelo usuario(a, b, c)

Exemplo:

Seja a equação: ax**2 + bx + c = 0, calcule as raizes da equação para a, b, c dados pelo usuario

"""
import math

def main():

    # Primeiro pedimos ao usuario os valores para a, b, c

    Valor_a = int (input ("Digite um numero para o a: "))
    Valor_b = int (input ("Digite um numero para o b: "))
    Valor_c = int (input ("Digite um numero para o c: "))

    # Agora com os valores de a, b, c temos que calcular o valor de delta
    # delta = b ** 2 - 4 * a * c

    delta = (Valor_b ** 2) - 4 * Valor_a * Valor_c

    # Em delta temos 3 opções: 
    # Delta > 0 (Temos duas raizes)
    # Delta < 0 (Não temos raizes reais)
    # Delta = 0 (Temos uma raiz)

    if delta >= 0: # Pode ser delta = 0 ou delta > 0, podemos calcular a raiz(s
        if delta > 0: # Temos duas raizes
            x1 = (- Valor_b + math.sqrt (delta)) / (2 * Valor_a)
            x2 = (- Valor_b - math.sqrt (delta)) / (2 * Valor_a) 

            print ("Para a = ", Valor_a, ", b = ", Valor_b, "e c = ", Valor_c,"temos duas raizes: ")
            print("x1 = ", x1, "x2 = ", x2)

        else: # delta = 0, temos uma raiz
            x1 = (- Valor_b) / (2 * Valor_a)
            print ("Para a = ", Valor_a, ", b = ", Valor_b, "e c = ", Valor_c,"temos uma raiz: ")
            print ("x1 = ", x1)


    else: # Delta < 0, não temos raizes reais
        print ("Para a = ", Valor_a, ", b = ", Valor_b, "e c = ", Valor_c, "Não temos raizes reais")

main()

#   #   #
##  ##  ##
### ### ###