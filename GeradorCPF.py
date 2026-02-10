"""projeto final da seção de lógica de programação básica
gerador automático de CPF
utiliza o módulo random p gerar os primeiros nove digitos do cpf
dps calcula os dois digitos verificadores e os adiciona ao cpf inicial
td com base na regra de cálculo do cpf
como produto, exibe um cpf válido e aleatorio
"""

import random

digitos_iniciais = ''
for digito in range(9):
    digitos_iniciais += str(random.randint(0, 9))

primeiro_digito_verificador = 0
for i in range(len(digitos_iniciais)):
    primeiro_digito_verificador += int(digitos_iniciais[i]) * (10 - i)

primeiro_digito_verificador = (primeiro_digito_verificador * 10) % 11
primeiro_digito_verificador = 0 if primeiro_digito_verificador > 9 else primeiro_digito_verificador

digitos_com_primeiro_verificador = digitos_iniciais + str(primeiro_digito_verificador)

segundo_digito_verificador = 0
for i in range(len(digitos_com_primeiro_verificador)):
    segundo_digito_verificador += int(digitos_com_primeiro_verificador[i]) * (11 - i)

segundo_digito_verificador = (segundo_digito_verificador * 10) % 11
segundo_digito_verificador = 0 if segundo_digito_verificador > 9 else segundo_digito_verificador

cpf_completo = digitos_com_primeiro_verificador + str(segundo_digito_verificador)

print(f"CPF gerado: {cpf_completo}")

"""possibilidades de melhoria:
- adicionar formatação ao cpf gerado 
- permitir ao usuário escolher quantos cpfs deseja gerar
"""