"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
 
print("a entrada deve ser SÓ de números")
entrada = input("insira um cpf para ser validado: ")
if len(entrada) == 11:
    try:
        cpf = int(entrada)
        cpf = entrada[:9]
        soma = 0
        contador = 10
        for digito in cpf:
            soma = soma + int(digito) * contador
            contador -= 1
        soma *= 10
        resto = soma % 11
        primeiro_digito = resto
        if resto > 9:
            primeiro_digito = 0
        if primeiro_digito == int(entrada[-2]):
            print(f"o primeiro dígito do cpf é válido")
        else:
            print(f"o primeiro dígito deveria ser {primeiro_digito}")
    except:
        print("insira somente números")
else:
    print("o cpf precisa possuir 11 dígitos")