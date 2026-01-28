"""dado um nome
transforme ele um uma nova string com caracteres separados por ponto
joao = j.o.a.o
"""

nome = input("digite seu nome: ")
cont = 0
tamanho_nome = len(nome)
novo_nome = '' 

while cont < tamanho_nome:
    novo_nome += nome[cont]
    novo_nome += '.'
    cont += 1
print(novo_nome)

"""calculadora com while
peça dois numeros ao user e um operador 
os operadores permitidos serão + - * /
exiba o resultado e continue pedindo esses valores
ate q o user queira sair
"""

print("abrindo a calculadora...")
while True:
    a = float(input("primeiro número: "))
    op = input("operador (+, -, *, /): ")
    b = float(input("segundo número: "))
    while op not in '+-*/':
        op = input("insira um operador válido: ")
    
    if op == '+':
        print(f"o resultado é {a + b}")
    elif op == "-":
        print(f"o resultado é {a - b}")
    elif op == "*":
        print(f"o resultado é {a * b}")
    else:
        print(f"o resultado é {a / b}")

    entrada = input("[c]ontinuar [s]air: ")
    if entrada == 's':
        break