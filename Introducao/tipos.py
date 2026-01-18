"""caracteristicas da tipagem do python
dinâmica - no momento da leitura do codigo o interpretador ja detecta o tipo
forte -
"""

"""str/string
sao textos que estão dentro de aspas
tanto simples como duplas 
como as aspas sao usadas pra colocar a string, pra ignorar essa funcao e realmente printar uma aspa
basta usar o caracter de escape barra invertida
ou utilizar aspas simples fora e duplas dentro e vice versa
"""
print("rielly", 'luiza')
print("\"rielly\"", "'luiza'")

"""int/integer
representa qualquer numero inteiro
tanto positivo quanto negativo
"""
print(0, 20, sep = " e ", end = " são inteiros\n")

"""float
representa qualquer numero do conjunto dos nums racionais
tanto positivo quanto negativo
"""
print(0.0, 2/5, sep = " e ", end = " são floats\n")

# a função type() retorna o tipo do argumento
print("Texto", type("Texto"))
print(-12, type(12))
print(1.2, type(1.2))

"""bool/boolean
possui dois valores: verdadeiro ou falso
é possivel comparar algo e saber se é true ou false
"""
print(10 == 10.0)
print(type(False))