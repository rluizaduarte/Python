# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'sobre dicionários, qual alternativa é a correta?',
        'Opções': ['são imutaveis', 'so pode indices numericos', 'armazena pares de chave e valor', 'não aceita valores mutaveis'],
        'Resposta': 'armazena pares de chave e valor'
    },
        {
        'Pergunta': 'sobre o método update(), qual é a alternativa correta?',
        'Opções': ['remove todos os itens do dicionário', 'atualiza ou adiciona pares chave-valor', 'retorna apenas os valores do dicionário', 'copia o dicionário para uma nova variável'],
        'Resposta': 'atualiza ou adiciona pares chave-valor'
    },
    {
        'Pergunta': 'o que o método get() faz quando a chave não existe?',
        'Opções': ['da erro', 'retorna 0', 'cria uma nova chave', 'retorna None'],
        'Resposta': 'retorna None'
    },
    {
        'Pergunta': 'sobre shallow copy, qual é a alternativa correta?',
        'Opções': ['cria um novo dicionário, porém os itens mutáveis compartilham a mesma referência', 'cria um novo dicionário com todos os itens independentes', 'n permite modificar o dicionário copiado', 'cria uma nova referência pro mesmo canto'],
        'Resposta': 'cria um novo dicionário, porém os itens mutáveis compartilham a mesma referência'
    },
        {
        'Pergunta': 'sobre o método setdefault(), qual é a alternativa correta?',
        'Opções': ['sempre substitui o valor da chave', 'remove a chave se ela existir', 'adiciona a chave se não existir e retorna o valor', 'retorna apenas as chaves do dicionário'],
        'Resposta': 'adiciona a chave se não existir e retorna o valor'
    },
]

contador_perguntas = 1
n_acertos = 0
for dicionario in perguntas:

    print(f"""
{contador_perguntas}° pergunta:
{dicionario['Pergunta']}
""")
    
    alternativa = 0
    for opcao in dicionario["Opções"]:
        print(f"{alternativa}) {opcao}")
        alternativa += 1

    print()
    resposta_usuario = input()
    while resposta_usuario not in "0, 1, 2, 3":
        print("Resposta inválida, tente novamente")
        resposta_usuario = input()
    print()

    if dicionario["Opções"][int(resposta_usuario)] == dicionario["Resposta"]:
        print(f"ai sim. vc acertou")
        n_acertos += 1
    else:
        print(f"errou, estude mais. a resposta correta era:")
        print(f"{dicionario["Resposta"]}")

    contador_perguntas += 1

print()
if n_acertos == len(perguntas):
    print(f"uau!!! vc eh um genio, acertou tudo!!")
else:
    print(f"vc acertou {n_acertos} de {len(perguntas)} perguntas")