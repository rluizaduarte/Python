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

"""desempacotamento
imaginando q a lista seja um pacote com coisas dentro
desempacotar seria criar novas variaveis para cada coisa dentro do pacote
"""

nomes = ["ricardo", "ryan", "victor"]
nome1, nome2, nome3 = nomes
# n vai funcionar se tiver menos variaveis do q itens no pacote e vice versa
print(nome1)

# tem como tb deixar o resto dos nomes em uma nova lista
nomes = ["ricardo", "ryan", "victor", "felipe", "luiza"]
nome1, nome2, *outros_nomes = nomes
print(nome1)
print(outros_nomes)

"""tuples/tuplas
são listas imutaveis
usados p armazenar dados q n devem ser alterados
a tupla eh um pouco mais eficiente q a lista
um dos jeitos de criar tupla eh so sem colchetes
ou, ainda, c parenteses no lugar dos colchetes
"""

cores = ("azul", "verde", "amarelo")
print(cores, type(cores))
# se isso fosse uma lista, poderia usar a prox linha
# cores[0] = "vermelho"
# mas como é uma tupla, n pode alterar