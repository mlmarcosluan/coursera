"""
Escreva um programa que receba um número ineitero na entrada e verifique se o número recebido possui
ao menos um dígito com um dígito adjacente igual a ele
"""

def main ():

    tamanho = input ("Digite um numero inteiro: ")
    numero = int (tamanho)
    passagens = len(tamanho) - 1
    
    n1 = numero % 10
    numero = numero // 10
    n2 = numero % 10
    numero = numero // 10
    
    sequencia = False
    while passagens > 0 and not sequencia:
        if n1 == n2:
            sequencia = True
        else:
            n1 = n2
            n2 = numero % 10
            numero = numero // 10
            passagens = passagens - 1

    if sequencia:
        print ("sim")
    else:
        print ("não")
main ()

#   #   #
##  ##  ##
### ### ###