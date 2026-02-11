"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# obs: o segundo digito eh calculado c base na entrada e n c base no possivel primeiro digito
# se colocar o primeiro e o segundo digito errados na entrada, ele vai dar um resultado p primeiro digito p combinar c o resto do cpf
# p segundo digito ele vai dar um resultado p combinar c entrada, mas o resultado do segundo digito n vai combinar c o primeiro digito, entao o cpf n vai ser valido

# ex: 12976798422 
# o primeiro digito calculado 9 
# o segundo é 7 
# tendo assim duas respostas
# 129.767.984-9? (4)
# 129.767.984-97

print("a entrada deve ser SÓ de números")
entrada = input("insira um cpf para ser validado: ")

if len(entrada) == 11:
    try:
        cpf = int(entrada)
        cpf_1 = entrada[:9]
        cpf_2 = entrada[:10]
        resultado_1 = 0
        contador_1 = 10
        resultado_2 = 0
        contador_2 = 11

        for digito in cpf_1:
            resultado_1 += int(digito) * contador_1
            contador_1 -= 1
        for digito in cpf_2:
            resultado_2 += int(digito) * contador_2
            contador_2 -= 1

        resultado_1 = (resultado_1 * 10) % 11
        resultado_2 = (resultado_2 * 10) % 11

        digito_final_1 = resultado_1 if resultado_1 <= 9 else 0
        digito_final_2 = resultado_2 if resultado_2 <= 9 else 0
        
        # p resolver o problema descrito la em cima
        # poderia calcular o primeiro digito e concatenar c a string cpf_1

        # apos o calculo correto dos dois digitos, uma nova var poderia ser criada
        # cpf_gerado q seria o cpf_2 concatenado c o digito dois
        # dessa forma o unico if aq seria cpf_enviado == cpf_gerado?
        
        if digito_final_1 == int(entrada[-2]):
            print(f"o primeiro dígito do cpf é válido")
        else:
            print(f"o primeiro dígito deveria ser {digito_final_1}")

        if digito_final_2 == int(entrada[-1]):
            print(f"o segundo dígito do cpf é válido")
        else:
            print(f"o segundo dígito deveria ser {digito_final_2}")
    
    except:
        print("insira somente números")
else:
    print("o cpf precisa possuir 11 dígitos")