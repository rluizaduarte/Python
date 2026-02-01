"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# um detalhe q mudaria um pouco seria importar a bliblioteca os
# essa bib permite limpar a tela do terminal
# import os

palavra_secreta = "enrolados"
# poderia guardar as letras acertadas em uma variavel do tipo string
# letras_acertadas = "" e ir concatenando ao longo dos acertos
palavra_escondida = len(palavra_secreta) * "_"
tentativas = 0

print("vamos brincar de forca")
print("dica: é um filme da disney")
print(f"\n{palavra_escondida}\n")

achou = False
while not achou:
    letra = input("chute uma letra: ").lower()
    if len(letra) > 1:
        print("n vale! digite so uma letra")
        continue

    tentativas += 1
    if letra in palavra_secreta:
        print(f"boa! acertou uma letra")
        # uma vez q tivesse a var de letras acertadas, a logica aq poderia ser simplesmente a do comando
        # for letra in palavra_secreta se a letra estiver em letras_acertadas, então print(letra) else print("*")
        # ou, ainda, criar uma nova var palavra_formada p ir colocando a letra acertada ou o * ao inves de printar 
        for i in range(len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                palavra_escondida = (
                palavra_escondida[:i] + letra + palavra_escondida[i + 1:]
                )
        print(f"\n{palavra_escondida}\n")
    else:
        print("\nessa letra n ta na palavra")
        print(f"vc ja tentou {tentativas}x")
        print("tente dnv\n")
    
    if palavra_escondida == palavra_secreta:
        print(f"voce acertou a palavra secreta: {palavra_secreta}")
        print(f"voce tentou {tentativas}x")
        achou = True

    # aq ou em qqr outra linha poderia usar os.system('cls') p limpar a tela