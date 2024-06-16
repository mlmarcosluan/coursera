"""
Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve:
Fizz se o número for divisivel por 3 e não por 5
Buzz se o número for divisível por 5 e não por 3
FizzBuzz se o número for divisível por 3 e por 5
"""
def div_3 (n):
    if n % 3 == 0:
        return True
    else:
        return False
    
def div_5 (n):
    if n % 5 == 0:
        return True
    else: 
        return False
    

def fizzbuzz (n):

    if div_3 (n) and div_5 (n):
        return "FizzBuzz"
    
    elif div_3 (n) and not div_5 (n):
        return "Fizz"
    
    elif not div_3 (n) and div_5 (n):
        return "Buzz"
    
    else:
        print (n)
        return n
    
#   #   #
##  ##  ##
### ### ###