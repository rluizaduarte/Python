"""formatação com f-strings
atalhos
f antes das aspas da string
variaveis dentro de chaves {}
s - string / d - inteiros / f - floats
.<n>f - numero de casas decimais
x - hexadecimal / o - octal / b - binario
(caractere)(> ou < ou ^)(quantidade)
> - direita / < - esquerda / ^ - centro
sinal + ou - ou espaço
+ - sempre mostra o sinal / - - só o sinal negativo
conversion flag !r / !s / !a
"""
nome = "ana"
print(f"{nome:-^20}")  
# a string fica c 20 caracteres e o nome fica no meio
print(f"{nome: >20}")
# a string fica c 20 caracteres e o nome fica à direita
print(f"{nome:=<20}")
# a string fica c 20 caracteres e o nome fica à esquerda

"""fatiamento de strings
[início:fim:passo]
"""
texto = "programação em python"
print(texto[:])
# do início até o final
print(texto[0:11])  
# do caractere 0 ao 10
print(texto[2:10:2])
# do caractere 13 até o final
print(texto[::-1])
# do final até o início (inverso)

"""função len
retorna o tamanho (número de caracteres) de uma string
"""
frase = "aprendendo python"
tamanho = len(frase)
print(f"a frase '{frase}' tem {tamanho} caracteres")