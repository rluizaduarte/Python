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
    if opcao not in "ial":
        os.system("cls")
        print("você não selecionou uma opção válida")
        continue
    else:
        if len(lista) < 1 and opcao in "al":
            if opcao == 'a':
                os.system("cls")
                print("n tem nada p apagar na sua lista")
                continue
            elif opcao == 'l':
                os.system("cls")
                print("sua lista ainda ta vazia. tente inserir algo")
                continue
        else:
            if opcao == 'i':
                item = input("nome do item: ")
                lista.append(item)
                os.system("cls")
                print("item adicionado na lista com sucesso")
            elif opcao == 'a':
                indice = int(input("indice do item para remover: "))
                try:
                    lista.pop(indice)
                    os.system("cls")
                    print("item removido da lista com sucesso")
                except:
                    os.system("cls")
                    print("o índice que vc informou é inválido")
            elif opcao == 'l':
                os.system("cls")
                lista_enumerada = enumerate(lista)
                for indice, item in lista_enumerada:
                    print(f"indice {indice} item {item}")
                