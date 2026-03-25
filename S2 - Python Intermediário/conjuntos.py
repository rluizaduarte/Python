"""introducao ao tipo set em python
o tipo set é um conjunto, a msm coisa q os conjuntos na matematica
(conjunto dos inteiros, conjunto dos numeros primos, etc)
graficamente na matematica os conjuntos sao representados pelo diagrama de venn
esse diagrama usa circulos pra representar os conjuntos e as intersecoes entre eles
são estruturas de dados q armazenam elementos unicos
eles n permitem elementos duplicados
são tipos de dados mutaveis
no entanto, so aceitam como conteudo tipos de dados imutaveis
pra criar um set basta usar chaves ou a classe set()
"""

# criando um set usando chaves
conjunto_a = {1, 2, 3, 4, 5}
print(conjunto_a)
# criando um set usando a classe
conjunto_b = set([4, 5, 6, 7, 8])
print(conjunto_b)

# um set vazio é considerado um dicionario
conjunto_vazio = {}
print(type(conjunto_vazio))

# passando um iteravel p classe ele considera cada elemento do iteravel como um elemento do set
conjunto_c = set("python")
# sets n aceitam elementos duplicados, ent ele vai eliminar os repetidos
print(conjunto_c)
# sets n tem ordem

# passando um iteravel usando chaves ele considera o iteravel inteiro como um elemento do set
conjunto_d = {"python"}
print(conjunto_d)

"""caracteristicas dos sets
geralmente sao mt eficientes p remover valores duplicados de um iteravel
naturalmente sao mt usados p fzr operacoes de conjuntos 
os sets sao iteraveis
no entanto, o problema é q eles n tem ordem garantida
ent se eu quiser manter a ordem, eu teria q usar outra ferramenta
outro problema tb é que n ele n aceita elementos mutaveis
m existe set dentro de set, lista dentro de set, dicionario dentro de set, etc
eles tb n tem indices
"""

#suponha uma lista com valores duplicados
lista_com_duplicados = [1, 2, 3, 4, 5, 1, 2, 3]
print(lista_com_duplicados)
# p remover os duplicados posso simplesmente converter a lista em um set
conjunto_sem_duplicados = set(lista_com_duplicados)
print(conjunto_sem_duplicados)

# sets sao iteraveis. posso usar for, in, not in
for elemento in conjunto_sem_duplicados:
    print(elemento)
print(3 in conjunto_sem_duplicados)
print(4 not in conjunto_sem_duplicados)

"""metodos
assim como os dicionarios, os sets tem metodos uteis
os principais sao add, update, clear e discard
"""

# o add() adiciona um elemento ao set
conjunto_sem_duplicados.add(6)
print(conjunto_sem_duplicados)

# o update() adiciona varios elementos ao set
# ele recebe um iteravel
conjunto_sem_duplicados.update([7, 8, 9])
print(conjunto_sem_duplicados)
#claramente n adiciona elementos q ja tem no set
conjunto_sem_duplicados.update([1, 2, 3])
print(conjunto_sem_duplicados)

# o discard() remove um elemento especifico do set
conjunto_sem_duplicados.discard(9)
print(conjunto_sem_duplicados)

# o clear() remove todos os elementos do set
conjunto_sem_duplicados.clear()
print(conjunto_sem_duplicados)

