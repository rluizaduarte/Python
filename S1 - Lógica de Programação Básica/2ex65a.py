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
# poderia usar if p n imprimir . na ultima letra

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
    # é interessante usar o isdigit c if ou try except p verificar se os nums sao validos
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

    # poderia usar entrada.lower() pra considerar respostas em maiusc
    entrada = input("[c]ontinuar [s]air: ")
    # poderia tb usar o startswith('s') pra ele aceitar qqr palavra q comeca c s
    if entrada == 's':
        break
    # os metodos podem ser usados na msm linha do input x = input().lower()