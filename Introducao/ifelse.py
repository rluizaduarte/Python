"""estruturas de decisão
essas estrutura permitem que o programa tome decisões
é possível que o programa siga caminhos diferentes
td isso dependendo de condições 
if = se
elif = senão se
else = senão
"""
idade = int(input("digite sua idade: "))
# se a condição for verdade, executa o bloco de código
if idade >= 18:
    print("vc eh maior de idade")
# se a condição for falsa, ainda é possível testar outra condição
elif idade >= 10:
    print("vc eh adolescente")
# se nenhuma das condições anteriores for verdade, ai sim executa o bloco de código do else
else:
    print("vc eh criança")

"""o q vai ser impresso no terminal depende
totalmente do valor digitado pelo usuário
se o usuário digitar 20, a saída será:
vc eh maior de idade
pq 20 é maior q 18
se o usuário digitar 15, a saída será:
vc eh adolescente
pq 15 não é maior q 18, mas é maior q 10
se o usuário digitar 5, a saída será:
vc eh criança
pq 5 não é maior q 18 nem maior q 10
"""

"""identação
os blocos q sao executados dependem da identação
esse tab é p respeitar q seja lido somente o q ta dentro da decisão tomada
se algo estiver fora dos blocos, será executado independente da decisão
"""
print("fim do programa")