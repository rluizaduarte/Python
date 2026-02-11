"""estruturas de repeticao
as estruturas permitem que um mesmo codigo repita ate que uma condição seja satisfeita
isso evita q tenha q repetir em varias linhas
é necessario q sempre tenha uma condição
sem objetivo, o programa fica rodando p smp
o cod fica preso nas linhas q estao dentro da identação do loop
"""

"""while/enquanto
enquanto algo for verdade, faça isso
cada vez que o bloco dentro do while for executado, o interpretador volta na condicao 
ele verifica se ainda é vdd e só continua dnv se for vdd
se a condicao n for mais vdd, o loop acaba
msm q a condicao se torne mentira no meio do loop, ele ainda vai terminar o bloco
"""

condicao = True
while condicao:
    print("isso vai se repetir p smp")
    # em algum momento, é necessario q a condição mude de valor p que o loop pare
    condicao = False
print("fim do loop")

"""break
é outra forma de sair de um loop
o break procura o loop mais proximo e sai dele
ele so para o loop mais perto (mais interno)
"""

while True:
    print("isso tbm vai se repetir p smp")
    # como n tem como a condição mudar, usamos o
    break
print("o break saiu do loop")

"""continue
o continue ignora o resto do bloco e volta p condicao
ele so afeta o loop mais proximo (mais interno)
nd abaixo do continue é executado
porem o q ta em cima do continue é executado normalmente
"""

contador = 0
while contador < 10:
    contador += 1
    print(contador)
    if contador == 5:
        continue
    print("esse numero n é 5")

"""while dentro de while
é possivel ter um loop dentro de outro loop
cada loop funciona de forma independente
o break e continue afetam apenas o loop mais proximo
o while de dentro roda x vezes enquanto o de fora roda 1 vez
"""

fora = 0
while fora < 3:
    print(f"fora: {fora}")
    dentro = 0
    while dentro < 3:
        print(f"  dentro: {dentro}")
        dentro += 1
    fora += 1

"""for/para
para cada item em um canto faça isso 
o for é usado pra iterar 
iterar é passar cada item de um grupo
um grupo pode ser uma lista, uma string, um range
"""

texto = "coder vision"
# o for cria uma variavel temporaria letra q passa por cada caracter do texto
for letra in texto:
    print(letra)

"""range 
o range é um iteravel tb
ele gera uma sequencia de numeros
pode ser usado pra controlar quantas vezes um loop vai rodar
range(inicio, fim, passo)
por padrão o inicio é 0 e o passo é 1
o ultimo numero n é incluido
"""

# 0, 1, 2, 3, 4
intervalo = range(5)
# 2, 3, 4, 5, 6, 7, 8, 9
intervalo = range(2, 10)
# 2, 4, 6, 8
intervalo = range(2, 10, 2)
# o range é iteravel ent eu posso acessar o item de indice 2 (terceiro item)
print(intervalo[2])

for numero in intervalo:
    print(numero, end = ", ")
print()

# range é mt usado tb p pegar multiplos de um numero por causa do step
print("multiplos de 7")
for numero in range(0, 100, 7):
    print(numero, end = ", ")
print()

# for com range
for contador in range(5):
    print(contador)

"""componentes do for
iterável - é o grupo de itens q vai ser percorrido (str, range)
iterador - é a variavel temporaria q vai pegar cada item do iteravel (letra, numero, contador)
next - é o processo de pegar o proximo item
iter - é o iterador do iteravel
"""

"""while vs for
o while é mais usado quando n se sabe quantas vezes o loop vai rodar
enquanto no for ja se sabe qnts vezes o loop vai rodar
as mesmas coisas q funcionam c while funcionam c for tb
continue, break, loops dentro de loops, else
"""