def maiusculas(frase):
    """ recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem """

    """ Na tabela ASSCII as letras maiusculas vão de 65 até 90"""
    letras_m = ""

    for letra in frase:
        letra_assc = ord(letra)

        if letra_assc >= 65 and letra_assc <= 90:
            letras_m += letra

    return letras_m

#   #   #
##  ##  ##
### ### ###