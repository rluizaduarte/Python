"""estruturas de repeticao
as estruturas permitem que um mesmo codigo repita ate que uma condição seja satisfeita
isso evita q tenha q repetir em varias linhas
é necessario q sempre tenha uma condição
sem objetivo, o programa fica rodando p smp
"""

"""while/enquanto
enquanto algo for verdade, faça isso
cada vez que o bloco dentro do while for executado, o interpretador volta na condicao 
ele verifica se ainda é vdd e só continua dnv se for vdd
se a condicao n for mais vdd, o loop acaba
"""

condicao = True
while condicao:
    print("isso vai se repetir p smp")
    # em algum momento, é necessario q a condição mude de valor p que o loop pare
    condicao = False
print("fim do loop")