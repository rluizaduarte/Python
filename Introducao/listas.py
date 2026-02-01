"""arrays/lists/vetor/listas
é uma estrutura de dados q armazena varios elementos
todos esses elementos ficam dentro de uma mesma variavel
as listas são mutaveis e iteráveis
se assemelha ao sentido real de lista
lista de compras ou lista de tarefas
armazena valores de qqr tipo inclusive na msm lista
"""

# a forma mais comum de criar uma lista eh c colchetes
nomes = ["ricardo", "ryan", "victor", "felipe"]
idades = [29, 15, 22, 18]
inf_ricardo = ["ricardo", 29, 1.75, True]
print(f"nomes: {nomes}")
print(f"idades: {idades}")
print(f"{inf_ricardo[0]} tem {inf_ricardo[1]} anos mede {inf_ricardo[2]}m")
print(f"{nomes[0]} é maior de idade? {inf_ricardo[3]}")
# as listas sao mutaveis
nomes[2] = "luiza"
idades[2] = 20
print(f"nomes atualizados: {nomes}")
print(f"idades atualizadas: {idades}")

"""metodos uteis
append - adiciona um elemento no final
insert - adiciona um elemento em uma posiçao especifica
pop - remove o ultimo elemento ou o elemento de uma posição especifica
del - remove um elemento de uma posição especifica
clear - limpa a lista removendo td
extend - estende a lista adicionando varios elementos
"""

lista = []
print("""
lista de compras""")

while True:
    escolha = input("""
    1 - ver lista
    2 - add item
    3 - remover item
    4 - limpar lista
    5 - sair
    """)

    if escolha not in "12345":
        print("escolha uma opção valida")
        continue
    else:
        if escolha == '1':
            print(lista)
        elif escolha == '2':
            item = input("nome do item: ")
            lista.append(item)
        elif escolha == '3':
            print("o ultimo item da lista foi removido")
            lista.pop()
        elif escolha == '4':
            lista.clear()
            print("lista limpa")
        else:
            print("saindo...")
            break