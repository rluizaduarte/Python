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

# acessando itens do dicionario (dados da pessoa)
print(pessoa["nome"])
# cada item do dic
for chave in pessoa:
    print(chave, pessoa[chave])