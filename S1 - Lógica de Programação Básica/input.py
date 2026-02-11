"""input
é uma função q coleta dados do user
por padrão, o input sempre retorna uma string
podemos passar uma string como argumento
essa string vai aparecer no terminal pro user
o programa n finaliza enquanto o user n interagir
podemos atribuir essa interação a alguma variavel
"""
nome = input("qual é o seu nome? ")
print(f"olá, {nome}!")
# o = dentro da variavel na f-string mostra o nome da variavel e o valor dela
print(f"{nome=}")

"""coerção
pra mudar o tipo padrao do input
basta colocar a função do tipo desejado antes do input
é preciso fazer essa coerção se vc quer fzr conta
caso n seja feita a coerção, a variael continua sendo trata como str
portanto, só é possivel concatenar e repetir
"""
idade = int(input(f"qual a sua idade, {nome}? "))
print(f"{nome} nasceu em {2026 - idade}")