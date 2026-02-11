# formatação de strings

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

"""interpolação com %
é uma forma antiga de formatar strings
as variaveis são passadas após o %
parece c o printf do c
"""
nome = "carlos"
idade = 25
mensagem = "%s tem %d anos" % (nome, idade)
print(mensagem)
# formatando floats
altura = 1.80
print("%s tem %.2f de altura" % (nome, altura))
# formatando com largura mínima
numero = 42
print("o número é %5d" % numero)  # largura mínima de 5
print("o número é %-5d!" % numero)  # alinhado à esquerda
# preenchendo com zeros
print("o número é %05d" % numero)  # preenchido com zeros
# formatando porcentagens
porcentagem = 0.2567
print("porcentagem: %.2f%%" % (porcentagem * 100))
# o %% é usado p representar o símbolo de porcentagem
print("progresso: 75%% concluído")

"""metodos uteis p str
1. split - divide uma str em determinado caracter
por padrao ele quebra a frase nos espaços em branco
ele devolve uma lista das palavras separadas
"""

frase = "python eh uma das : linguagens mais conhecidas"
palavras = frase.split()
print(palavras)

# o split tb pode receber um argumento q seria o q ele vai usar p dividir as strings
palavras = frase.split(":")
print(palavras)

"""
2. strip - remove espaços em branco no começo e no fim da str
n remove espaços no meio da str
"""

texto = "    ola, mundo!    "
print(f"'{texto}'")
texto_limpo = texto.strip()
print(f"'{texto_limpo}'")

# sptrip pode recber argumentos p remover caracteres específicos
texto2 = "###bem vindo!!!###"
print(f"'{texto2}'")
texto2_limpo = texto2.strip("#!")
print(f"'{texto2_limpo}'")

"""
3. join - junta uma lista de str em uma única str
eh o inverso do split
tem q definir um separador p juntar as strs
o separador é a str q vai ficar entre as palavras
"""

palavras = ["python", "eh", "uma", "linguagem", "incrivel"]
frase = "&&&".join(palavras)
print(frase)  