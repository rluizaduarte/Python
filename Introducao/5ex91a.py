"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []
while True:
    print("selecione uma opção")
    opcao = input("[I]nserir [A]pagar [L]istar: ").lower()
    # a cadeia de if poderia ser mais simples
    # se é i, se é a, se é l ou se n é nenhum desses
    if opcao not in "ial":
        os.system("cls")
        print("você não selecionou uma opção válida")
        continue
        # n precisa desse continue
    else:
        if len(lista) < 1 and opcao in "al":
            if opcao == 'a':
                os.system("cls")
                print("n tem nada p apagar na sua lista")
                continue
                # n precisa desse tb
            elif opcao == 'l':
                os.system("cls")
                print("sua lista ainda ta vazia. tente inserir algo")
                continue
                # nem desse
        else:
            if opcao == 'i':
                item = input("nome do item: ")
                lista.append(item)
                os.system("cls")
                print("item adicionado na lista com sucesso")
            elif opcao == 'a':
                indice = int(input("indice do item para remover: "))
                try:
                    # poderia colocar o int(indice) aq
                    lista.pop(indice)
                    os.system("cls")
                    print("item removido da lista com sucesso")
                # except index error
                except:
                    os.system("cls")
                    print("o índice que vc informou é inválido")
                # por fim ainda podia colocar except exception q pega qqr erro
                # a saida seria "erro desconhecido" ou outra cs
            elif opcao == 'l':
                os.system("cls")
                lista_enumerada = enumerate(lista)
                for indice, item in lista_enumerada:
                    print(f"indice {indice} item {item}")
                