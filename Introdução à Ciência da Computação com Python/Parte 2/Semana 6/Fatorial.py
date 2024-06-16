def fatorial (n):
    if n < 1: # Se n < 1 sabemos que o fatorial é 1
        return 1
    else: # Caso n > 1 temos que fatorial de n é n * (n - 1)!
        return n * fatorial (n - 1)
    
#    #    #
##   ##   ##
###  ###  ###