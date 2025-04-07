#Aluna: Gabrielly Soares Alcântara Mota
#Curso: Análise e desenvolvimento de sistemas


# lista de estudantes vazia para coletar informações
listaEstudantes = []
# enquanto for verdade mostre o menu principal
while True:
    # menu principal
    print("----- [MENU PRINCIPAL] -----")
    print()
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.")
    print()

    # coletando a opção
    opcao = input("Informe a opção desejada: ")

    # se a opção for 1, mostre o menu de operações enquanto for verdade
    if opcao == "1":
        while True:
            print()
            print(f"Você escolheu a opção válida ({opcao})")
            print()

            # mostrando o menu de operações
            print(f"★★★★★ [ESTUDANTES] MENU DE OPERAÇÕES ★★★★★")
            print()
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            print()

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print()

            # se for opção 1, peça para que inclua alunos na lista
            if opcao2 == "1":
                print()
                print("=========== INCLUIR ===========")
                print()
                # pedir nome ao usuário
                nome = input("Informe o nome do estudante: ")
                print("Pressione ENTER para continuar.")
                print()
                print("=" * 30)
                # colocar o "nome" na listaEstudantes
                listaEstudantes.append(nome)

            # se for opção 2, exiba a lista de alunos
            elif opcao2 == "2":
                print()
                print("=========== LISTA ===========")
                print()
                # se a lista de estudantes estiver vazia, informe ao usuário
                if len(listaEstudantes) == 0:
                    print("Não há estudantes cadastrados.")
                    print()
                    print("=" * 29)
                # senão, exibir a lista
                else:
                    print("\nLista de Estudantes:")
                    for i, estudante in enumerate(listaEstudantes,start=1):
                        print(f"{i}. {estudante}")
                    print("Pressione ENTER para continuar.")
                    print()
                    print("=" * 29)


                    # senão, se for uma dessas opções, mostre que está em desenvolvimento
            elif opcao2 == "3" or opcao2 == "4":
                print()
                print(f"Você escolheu a opção válida ({opcao2})")
                print()
                # mostrando que está em desenvlvimento
                print()
                print("====== ATUALIZAÇÃO ======")
                print()
                print("    EM DESENVOLVIMENTO")
                print()
                print("=" * 25)
                print()

            # senão, se a opção for = 9, volte para o menu principal
            elif opcao2 == "9":
                print()
                print("Você escolheu voltar para o [MENU PRINCIPAL]")
                print()
                break
            # senão for nenhuma dessas, considere inválida
            else:
                print()
                print("Você escolheu uma opção INVÁLIDA, tente novamente!")
                print()

    # senão, se for uma dessas opções, informe que está em desenvolvimento
    elif opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        print()
        print("====== ATUALIZAÇÃO ======")
        print()
        print("    EM DESENVOLVIMENTO")
        print()
        print("=" * 25)
        print()

    # senão, se a opção for = 9, volte para o menu principal
    elif opcao == "9":
        print()
        print("Você escolheu sair!")
        break
    else:
        print()
        print("Você escolheu uma opção INVÁLIDA, tente novamente!")
        print()