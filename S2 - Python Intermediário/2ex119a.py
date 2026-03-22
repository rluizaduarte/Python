"""
Crie funções que duplicam, triplicam e quadruplicam o numero recebido como parametro
"""

def produto(fator):
    def calcular(numero):
        return numero * fator
    return calcular

duplica = produto(2)
triplica = produto(3)
quadruplica = produto(4)
quintuplica = produto(5)

for numero in [1, 2, 3, 4, 5]:
    print(f"dobro de {numero} = {duplica(numero)}")
    print(f"triplo de {numero} = {triplica(numero)}")
    print(f"quadruplo de {numero} = {quadruplica(numero)}")
    print(f"quintuplo de {numero} = {quintuplica(numero)}")