"""try/except
serve para tratar erros que podem acontecer
tenta executar o bloco try
se um erro acontecer, o bloco except é executado
"""

entrada = input("digite um numero para ser dobrado: ")
try:
    print(f"você digitou {entrada}")
    # na linha q ele n conseguir executar, ele ja manda p exceção
    numero_float = float(entrada) 
    print(f"o dobro de {numero_float} é {numero_float * 2}")
except:
    print(f"{entrada} não é um número")

"""try/except especifico
é possivel tratar erros específicos
p isso, precisa saber o nome do erro
"""

entrada = input("digite um numero para ser dobrado: ")
try:
    print(f"você digitou {entrada}")
    numero_float = float(entrada) 
    print(f"o dobro de {numero_float} é {numero_float * 2}")
except ValueError:
    # trata apenas erros do tipo ValueError q é quando n consegue converter p numero
    print(f"{entrada} não é um número válido")