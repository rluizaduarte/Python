
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

# sem o try except
if entrada_1.isdigit():
    ...
else:
    ...

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada_2 = int(input("digite a hora atual (0-23): "))
try:
    hora = int(entrada_2)
    # variavel de comparação errada. deveria ser "hora" e não "entrada_2"
    if (entrada_2 <= 11): 
        # o certo seria hora >= 0 and hora <= 11 (0 <= hora <= 11)
        print("bom dia!")
    elif (entrada_2 <= 17):
        # p deixar mais legivel, poderia definir o intervalo aq tb, mas n muda na logica
        print("boa tarde!")
    elif (entrada_2 <= 23):
        print("boa noite!")
    else: 
        # n vai cair aqui pq no primeiro if n tem hora >= 0
        print("você não digitou uma hora válida")
except:
    print("você não digitou um número")

# outra opção aqui seria usar o isdigit também
 
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("digite o seu primeiro nome: ")
tamanho_nome = len(primeiro_nome)

# por segurança, poderia verificar se o user de fato digitou algo. um "if nome" ou um "if tamanho_nome > 0" 

if tamanho_nome <= 4:
    print("seu nome eh curto")
elif tamanho_nome <= 6:
    print("seu nome eh normal")
else:
    print("seu nome eh mt grande")