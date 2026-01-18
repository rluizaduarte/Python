"""formatação de strings
formatted strings ou f-strings
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