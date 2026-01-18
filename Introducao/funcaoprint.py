"""função print
usada p exibir/imprimir algo na tela
"""

# como toda funcao, recebe argumentos
print(12) # 12 é um argumento
# argumentos podem ser separados por virgulas
print (12, 34)

"""12 é um argumento não nomeado
argumento nomeado precisa colocar antes o nome e dps o valor
"""

"""sep é um argumento nomeado
p mudar o separador de argumentos padrão que é " "
basta usar o sep como argumento
"""
print(12, 34, sep = "")
print(98612, 2001, sep = '-')

"""end é um argumento nomeado
p mudar o q vem no final da impressao q por padrao é new line
basta usar o end como argumento
"""
print(1, end = ', ')
print(2, end = ".")