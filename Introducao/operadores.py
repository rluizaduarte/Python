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
print("10 é igual a 10? ", igualdade)
diferenca = 10 != 8
print("10 é diferente de 8? ", diferenca)
maior_que = 10 > 8
print("10 é maior que 8? ", maior_que)
menor_que = 10 < 8
print("10 é menor que 8? ", menor_que)
maior_ou_igual = 10 >= 10
print("10 é maior ou igual a 10? ", maior_ou_igual)
menor_ou_igual = 8 <= 10
print("8 é menor ou igual a 10? ", menor_ou_igual)