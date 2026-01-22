"""aritmericos/matematica
o python, naturalmente, entende a prioridade dos operadores
"""

adicao = 10 + 10
print("10 + 10 =", adicao)
subtracao = 20 - 12.5
print("20 - 12.5 =", subtracao)
multiplicacao = 3.14 * 10
print("3.14 * 10 =", multiplicacao)
# a divisao sempre retorna numero float
divisao = 10 / 3
print("10 / 3 =", divisao)
# a divisão inteira faz truncamento e ignora as casas decimais
divisao_inteira = 10//3
print("parte inteira de 10 / 3 =", divisao_inteira)
modulo = 10 % 3
print("resto da divisao de 10 / 3 =", modulo)
exponenciacao = 2 ** 10
print("2 elevado a 10 =", exponenciacao)

"""peculiaridades
alem da soma, o + é usado pra concatenar str
alem da multiplicacao, o * é usado pra repetir u:ma str
"""
concatenacao = "joao" + " " + "paulo"
print("joao + paulo =", concatenacao)
a_dez_vezes = "A" * 10
print("a dez vezes ou dez vezes a =", a_dez_vezes)

"""de comparação/relacionais
são usados para comparar valores
retornam booleanos
"""
igualdade = 10 == 10
print("10 é igual a 10?", igualdade)
diferenca = 10 != 8
print("10 é diferente de 8?", diferenca)
maior_que = 10 > 8
print("10 é maior que 8?", maior_que)
menor_que = 10 < 8
print("10 é menor que 8?", menor_que)
maior_ou_igual = 10 >= 10
print("10 é maior ou igual a 10?", maior_ou_igual)
menor_ou_igual = 8 <= 10
print("8 é menor ou igual a 10?", menor_ou_igual)

"""logicos
são usados p combinar duas ou mais condições
retornam booleanos
isso E aquilo
isso OU aquilo
não isso
"""
# e logico so sera verdadeiro se os dois lados forem verdade
e_logico = (10 > 8) and (10 == 10)
print("(10 > 8) e (10 == 10)?", e_logico)
# ou logico vai ser verdadeiro se pelo menos um dos lados for verdadeiro tb
ou_logico = (10 > 8) or (10 < 8)
print("(10 > 8) ou (10 < 8)?", ou_logico)
# nao logico é o inverso da condição
nao_logico = not(10 > 8)
print("não (10 > 8)?", nao_logico)

"""avaliação de curto circuito
o python para de avaliar assim que o resultado é conhecido
assim q uma condição for suficiente para determinar o resultado
apenas um "false" em um "e" torna tudo falso
apenas um "true" em um "ou" torna tudo verdadeiro e
a primeira condição true em um ou é o valor retornado
"""

"""in e not in
strings são iteráveis (permite navegar item por item)
servem p ver se um item ta dentro ou n de uma string
"""
nome = "rielly"
tem_r = "r" in nome
print("tem a letra 'r' em 'rielly'?", tem_r)
tem_z = "z" in nome
print("tem a letra 'z' em 'rielly'?", tem_z)