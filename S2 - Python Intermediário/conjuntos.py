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