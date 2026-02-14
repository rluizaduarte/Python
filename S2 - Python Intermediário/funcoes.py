"""introdução às funções no python
funcoes sao receitas prontas que dao como retorno alguma coisa
se eu ja sei como se faz uma conta de soma, eu so jogo os nums e a receita me retorna o resultado
o objetivo da funcao é fazer c q se tenha ja uma pessoa q faz o trabalho
quantas vezes eu quiser
isso evita repetir tantas vezes o mesmo codigo
print() é uma funçao
"""

"""caracteristicas
recebe valores como parametros (argumentos)
pode retornar um valor especifico c base no codigo q tiver dentro
por padrao as funcoes retornam none mas a palvra return faz vc mudar isso
uma funcao pode ser declarada com a palavra chave def
def nome_da_funcao(argumentos) 
"""

# definindo a função sem parametros
def imprimir():
    # td q ta dentro desse bloco vai ser executado quando a funcao for chamada
    print("olá")
# chamando a funcao e n preciso mandar nada p ela
imprimir()

# definindo uma função com parametros
def imprimir_isso(coisa_a, coisa_b, coisa_c):
    print(coisa_a, coisa_b, coisa_c)
    # essas variaveis coisa a coisa b e coisa c so existem dentro da funcao
# chamando a funcao e mandando as coisas
imprimir_isso("ola", "hello world", 22)

# a mesma funcao chamada varias vezes ecnonomiza linha pq n precisa ficar escrevendo td dnv
def imprimir_a_soma(numero_1, numero_2):
    print(f"o primeiro numero q vc informou eh {float(numero_1)}")
    print(f"o segundo numero q vc informou eh {float(numero_2)}")
    print(float(numero_1) + float(numero_2))
# chamando a msm funcao varias vezes sem precisar ficar digitando a msm coisa
imprimir_a_soma(5, 33)
imprimir_a_soma(33.9, 44)
imprimir_a_soma("78", "99")

# podemos tb definir um valor padrao p o argumento ai se ele n manda o valor, ent usa o q definiu
def saudacao(nome = "usuario"):
    print(f"ola, {nome}!")
    print("bem vindo")
# sem passar nada, ele usa o nome q ja ta definido la
saudacao() 
# passando algo, ele muda o q ja ta definido pelo seu valor
saudacao("rielly")

"""argumentos nomeados e nao nomeados em funcoes
nomeado tem nome com sinal de igual
nao nomeado recebe apenas o argumento
os argumentos na funcao imprimir soma são posicionais
isso significa q a ordem/posicao q eles sao colocados dentro do parentese é significante
esses saoo nao nomeados
os nomeados especificam q a ordem n faz diferença
"""

def ola_mundo(palavra_1, palavra_2):
    print(palavra_1, palavra_2)
# argumentos posicionais 
ola_mundo("mundo", "ola")
# arfumentos nomeados
ola_mundo(palavra_2 = "mundo", palavra_1 = "ola")

# é possível mandar argumentos posicionais antes dos argumentos nomeados na msm chamada de função
# mas n é possivel o contrario
ola_mundo("ola", palavra_2="mundo")
# ola_mundo(palavra_1 = "ola", "mundo")

"""escopo
é o local q o codigo tem acesso
global - todo codigo é alcancavel
local - apenas nomes do msm local podem ser alcançados
o eh definido dentro da funcao eh local, ou seja, fica protegido la
as variaveis dentro da funcao n existem p o codigo fora da funcao
no entanto, as variaveis fora da funcao definidas antes existem dentro da funcao
"""

a_global = 5
def escopo_funcao():
    print(a_global)
    a_local = 15
    print(a_local)
# o a_local n pode ser acessado aq
# o a_global so pode ser acessado pq foi definido antes da declaracao da funcao
# e pq so chamamos a funcao dps de declarar a_global
escopo_funcao()

# a palavra global antes da var faz c que uma var do escopo EXTERNO tenha o mesmo valor no escopo INTERNO
x = 10
def escopo():
    global x
    # x tem valor 10 ainda
    print(x)
    x += 10
    # como o x da funcao eh o global, isso altera o x de fora
    print(x)
print(x, "antes de chamar a funcao")
escopo()
print(x, "dps de chamar a funcao")

# o escopo mais interno sempre procura a variavel mais perto p usar

"""retorno/return
a palavra return faz com q a funcao retorne algo
como em mat, o retorno seria o resultado da conta, a imagem
a funcao pode retornar qualquer tipo de valor, como string, numero, lista, dicionario, etc
o return tb pode ser usado p sair da funcao, ou seja, o codigo dps do return n vai ser executado
depende da função se ela vai ter retorno ou n
"""

# f(x) = a + b
def soma(numero_1, numero_2):
    # a funcao devolve a soma dos dois numeros e dps encerra 
    return numero_1 + numero_2
    # td q vier dps do return vai ser ignorado
    print("isso n vai ser impresso")
# posso guardar o resultado da funcao em uma variavel
resultado = soma(33, 44)
print(resultado)
