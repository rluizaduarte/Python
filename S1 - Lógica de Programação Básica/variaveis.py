"""variaveis
guarda espaço na memoria do pc
sao caixinhas rotuladas (espaços com apelidos)
cada caixa tem que ter um nome
o nome da variavel n pode começar com numero
a pep8 indica q esses nomes comecem c letra min, 
podendo haver num dps e underline p simular espaço
cada variavel, assim como na mat, possui um valor
o operador = é usado pra atribuição da variável 
"""

# ex: nome_variavel = valor
nome_completo = "pedro henrique"
idade = 15

# agr so precisa mudar o valor e n o resto do codigo]
nome_completo = "julia vieira"
idade = 49
maior_de_idade = idade >= 18
ano_de_nascimento = 2026 - idade
print(nome_completo, "é maior de idade?", maior_de_idade)
print("o ano de nascimento de", nome_completo, "é", ano_de_nascimento)

"""por convenção
variáveis constantes (q n mudam de valor) ficam c nome maiusculo
enquanto variáveis normais ficam c nome minusculo
"""

# velocidade atual do carro
velocidade = 61
# lugar q o carro ta (em km)
local_carro = 90
# velocidade max permitida no primeiro radar
VELOCIDADE_MAX_RADAR = 60
# lugar q o primeiro radar ta (em km)
LOCAL_RADAR = 100
# ate q distancia do radar o motorista começa a ser multado
RADAR_RANGE = 1 # ele pega carros q estao no km 99 ate o km 101

"""coisas q aumentam a complexidade do código:
- estruturas condicionais aninhadas (if dentro de if)
- mts condições no msm if
- loops aninhados (for dentro de for)
- funções/métodos muito longos (mto código dentro de uma função)
"""

# uma forma de verificar se o carro vai ser multado
if velocidade > VELOCIDADE_MAX_RADAR:
    print("a velocidade do carro é maior q a permitida no radar")
if local_carro >= (LOCAL_RADAR - RADAR_RANGE) and local_carro <= (LOCAL_RADAR + RADAR_RANGE):
    print("o carro esta dentro do alcance do radar")
if (velocidade > VELOCIDADE_MAX_RADAR) and (local_carro >= (LOCAL_RADAR - RADAR_RANGE) and local_carro <= (LOCAL_RADAR + RADAR_RANGE)):
    print("o carro sera multado")

# outra forma de verificar se o carro vai ser multado
velocidade_acima = velocidade > VELOCIDADE_MAX_RADAR
carro_no_radar = (local_carro >= (LOCAL_RADAR - RADAR_RANGE)) and (local_carro <= (LOCAL_RADAR + RADAR_RANGE))
if velocidade_acima and carro_no_radar:
    print("o carro sera multado")

# ainda há outras formas de deixar o codigo mais "enxuto"