
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada_1 = input("digite um número inteiro: ")
try:
    numero = int(entrada_1)
    if (numero % 2) == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
except:
    print(f"{entrada_1} não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada_2 = int(input("digite a hora atual (0-23): "))
try:
    hora = int(entrada_2)
    if (entrada_2 <= 11):
        print("bom dia!")
    elif (entrada_2 <= 17):
        print("boa tarde!")
    elif (entrada_2 <= 23):
        print("boa noite!")
    else: 
        print("você não digitou uma hora válida")
except:
    print("você não digitou um número")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("digite o seu primeiro nome: ")
tamanho_nome = len(primeiro_nome)
if tamanho_nome <= 4:
    print("seu nome eh curto")
elif tamanho_nome <= 6:
    print("seu nome eh normal")
else:
    print("seu nome eh mt grande")