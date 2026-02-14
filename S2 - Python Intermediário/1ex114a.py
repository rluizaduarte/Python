# Exercicios com funcoes

"""
Crie uma função que multiplca todos os argumentos não nomeados recebidos
Retorne o total para uma variavel e imprima o resultado
"""

# poderia tratar os valores

def multiplica(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

total = multiplica(2, 3, 4)
print(total)
tupla_total = (9, 27, 44)
novo_total = multiplica(*tupla_total)
print(novo_total)

"""
Crie uma função que diz se um numero é par ou impar
Retorne o resultado para uma variavel e imprima o resultado
"""

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é par"
    return f"{numero} é impar"
    # poderia retornar só true ou false
    # return numero % 2 == 0
    
print(par_ou_impar(10))
print(par_ou_impar(11))