"""
Dado um numero inteiro digitado pelo usuario temos que verificar se tem dois numeros adjacente 
iguais
"""

def main ():

    tamanho = input ("Digite um numero inteiro")
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
        print ("O numero digitado contem numeros adjacentes iguais")
    else:
        print ("O numero digitado não contem numeros adjacentes iguais")

main ()

#   #   #
##  ##  ##
### ### ###