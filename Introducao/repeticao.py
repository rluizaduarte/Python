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
