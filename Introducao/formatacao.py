#formatação de strings

"""formatted strings ou f-strings
são strings q permitem variaveis e textos formatados
as variaveis precisam ficar entre chaves {}
a string precisa começar com f ou F
podemos usar uma variavel pra guardar a f-string
ou podemos usar a f-string diretamente no print
podemos usar formatações dentro das chaves
"""
nome = "joao"
altura = 1.75
peso = 80.5
imc = peso / (altura ** 2)
mensagem = f"{nome} tem {altura:.2f} de altura e pesa {peso}kg"
print(mensagem)
print(f"o imc de {nome} é {imc:.2f}")

"""função format
é uma função nativa das strings
as variaveis são passadas como argumentos
as chaves {} indicam onde as variaveis serão inseridas
a função format respeita a ordem dos argumentos
podemos usar índices nas chaves para mudar a ordem
é possível tb repetir argumentos
e nomear argumentos usando chave=valor
"""
nome = "maria"
idade = 30
mensagem = "{} tem {} anos".format(nome, idade)
print(mensagem)
string = "{} nasceu em {}"
print(string.format(nome, "são paulo"))

# repetindo argumentos
true = "verdadeiro"
false = "falso"
string = "3 > 5? {0} 4 == 5? {0} 8 < 10? {1}"
print(string.format(false, true))

# nomeando argumentos
cidade = "recife"
habitantes = 10000000
estado = "pernambuco"
string = "{0} é a capital de {e} e tem {h} habitantes"
print(string.format(cidade, e=estado, h=habitantes))