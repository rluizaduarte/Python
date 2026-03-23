"""tipo de dados dict (dicionarios)
sao estruturas de dados do tipo par de CHAVE e VALOR
chave seria o indice, valor seria o conteudo
as chaves nesse caso podem ser qualquer tipo imutavel da linguagem 
(string, int, float, tuple, bool)
dict é mutável, assim como a lista
nome_do_dicionario = {chave : valor}
"""

# para representar os dados de uma pessoa com um dicionario
pessoa = {
    # é importante colocar a virgula p separar os itens
    "nome" : "beatriz",
    "idade" : 45,
    "altura" : 1.65,
    "peso" : 60,
    "hobbies" : ["correr", "nadar", "cozinhar"],
    # um dos itens do dicionario pode inclusive ser outro dicionario
    "endereço" : {
        "rua" : "rua A",
        "numero" : 123,
    }
    #ou, ainda, uma lista de dicionarios
    # "endereços" : [
    #     {
    #         "rua" : "rua A",
    #         "numero" : 123,
    #     },
    #     {
    #         "rua" : "rua B",
    #         "numero" : 456,
    #     }
    # ]
}

"""manipulando chaves e valores
"""

# acessar itens do dicionario (dados da pessoa)
print(pessoa["nome"])
# cada item do dic
for chave in pessoa:
    print(chave, pessoa[chave])

# adcionar itens ao dicionario 
pessoa["email"] = "beatriz@email.com"
#nome do dic[chave inexistente] = valor
print(pessoa)

# apagar itens do dicionario
del pessoa["peso"]
# del nome do dic[chave]
print(pessoa)

# o dunder len() retorna o numero de chaves do dic
print(pessoa.__len__())
print(len(pessoa))

"""métodos úteis p dicionarios
"""

print(pessoa.keys())
#retorna as chaves

print(pessoa.values())
#retorna os valores

print(pessoa.items())
#retorna uma lista de tuplas q cada tupla é um par chave-valor
# uma boa forma de percorrer o dicionario eh usando esse metodo
for chave, valor in pessoa.items():
    print(chave, valor)

print(pessoa.setdefault("sobrenome", "mendonca"))
# o setdefault() é um metodo q recebe uma chave e um valor
# se a chave n existir no dic, ele adiciona a chave com o valor e retorna
# se a chave ja existir, ele n altera o valor e retorna o valor existente

print(pessoa.get("sobrenome"))
# tambem recebe a chave e retorna o valor
# mas, por padrao, se a chave n existir, ele retorna None
# posso passar um segundo parametro p o get() q seria o valor padrao caso a chave n exista
print(pessoa.get("peso", "peso nao encontrado"))

pessoa_copia = pessoa.copy()
print(pessoa_copia)
# retorna uma copia rasa (shallow copy)

# atribuição: aponta p mesmo canto. se eu alterar um, o original altera
# shallow copy: cria um novo, mas os itens mutaveis ainda apontam p mesma ref. mudar a lista em um altera no outro
# deep copy: cria um novo e os itens mutaveis tb sao copiados. muda em um n muda no outro 

pessoa.pop("sobrenome")
# apaga um item c a chave especificada 
# mas ele ainda retorna o valor ent eu posso atribuir a uma var
idade = pessoa.pop("idade")
print(idade)
print(pessoa)

ultimo_item = pessoa.popitem()
# apaga o ultimo item adicionado e tb retorna um par chave-valor como tupla
print(ultimo_item)
print(pessoa)

pessoa.update({
    "sobrenome" : "mendonca", 
    "peso" : 60
    })
# atualiza o dicionario com itens novos ou modificando itens antigos
# esse metodo tb pode receber qqr iteravel como valor tipo lista ou tupla
tupla = (("sobrenome", "outro"), ("peso", 10))
pessoa.update(tupla)
print(pessoa)
lista = [["sobrenome", "qualquer outro"], ["peso", 20]]
pessoa.update(lista)
print(pessoa)