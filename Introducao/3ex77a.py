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

palavra_secreta = "enrolados"
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