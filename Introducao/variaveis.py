"""variaveis
guarda espaço na memoria do pc
sao caixinhas rotuladas (espaços com apelidos)
cada caixa tem que ter um nome
o nome da variavel n pode começar com numero
a pep8 indica q esses nomes comecem c letra min, 
podendo haver num dps e underline p simular espaço
cada variavel, assim como na mat, possui um valor
o operador = é usado pra atribuição da variável 
"""

# ex: nome_variavel = valor
nome_completo = "pedro henrique"
idade = 15

# agr so precisa mudar o valor e n o resto do codigo]
nome_completo = "julia vieira"
idade = 49
maior_de_idade = idade >= 18
ano_de_nascimento = 2026 - idade
print(nome_completo, "é maior de idade?", maior_de_idade)
print("o ano de nascimento de", nome_completo, "é", ano_de_nascimento)
