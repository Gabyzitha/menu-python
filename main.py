# Aluna: Gabrielly Soares Alcântara Mota
# Curso: Análise e desenvolvimento de sistemas


# lista de estudantes vazia para coletar informações
lista_estudantes = []
# enquanto for verdade mostre o menu principal
while True:
    # menu principal
    print("----- [MENU PRINCIPAL] -----\n")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.\n")

    # coletando a opção
    opcao = input("Informe a opção desejada: ")

    # se a opção for 1, mostre o menu de operações enquanto for verdade
    if opcao == "1":
        while True:
            print(f"Você escolheu a opção válida ({opcao})\n")

            # mostrando o menu de operações
            print(f"★★★★★ [ESTUDANTES] MENU DE OPERAÇÕES ★★★★★\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.\n")

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print(f"Você escolheu a opção válida ({opcao2})\n")

            # se for opção 1, peça para que inclua alunos na lista
            if opcao2 == "1":
                print("=========== INCLUIR ===========")

                # pedir código,nome e cpf ao usuário
                while True:
                    codigo = int(input("\nInforme o código do estudante: "))
                    nome = input("Informe o nome do estudante: ")
                    cpf = input("Informe o CPF do estudante: ")

                    # coloca essas informações em um dicionário
                    dados = {"código": codigo, "nome": nome, "cpf": cpf}
                    # coloca esse dicionário na lista_estudantes
                    lista_estudantes.append(dados)
                    print("\nEstudante cadastrado com sucesso!\n")

                    if input("Deseja cadastrar um novo contato (s/n)? ") == "n":
                        break

                print("Pressione ENTER para continuar.\n")
                print("=" * 30)

                # colocar o "nome" na listaEstudantes
                # dicionario vazio


            # se for opção 2, exiba a lista de alunos
            elif opcao2 == "2":
                print("=========== LISTA ===========\n")
                # se a lista de estudantes estiver vazia, informe ao usuário
                if len(lista_estudantes) == 0:
                    print("Não há estudantes cadastrados.\n")
                    print("=" * 29)
                # senão, exibir a lista
                else:
                    print("Lista de Estudantes:\n")
                    for i, dado in enumerate(lista_estudantes):
                        print(f"{i + 1}", dado)
                    print("Pressione ENTER para continuar.\n")
                    print("=" * 29)


            # senão, se for uma dessas opções, mostre que está em desenvolvimento

            elif opcao2 == "3" or opcao2 == "4":
                print(f"Você escolheu a opção válida ({opcao2})\n")
                # mostrando que está em desenvlvimento
                print("====== ATUALIZAÇÃO ======\n")
                print("    EM DESENVOLVIMENTO\n")
                print("=" * 25)

            # senão, se a opção for = 9, volte para o menu principal
            elif opcao2 == "9":
                print("Você escolheu voltar para o [MENU PRINCIPAL]\n")
                break
            # senão for nenhuma dessas, considere inválida
            else:
                print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")

    # senão, se for uma dessas opções, informe que está em desenvolvimento
    elif opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        print("====== ATUALIZAÇÃO ======\n")
        print("    EM DESENVOLVIMENTO\n")
        print("=" * 25)

    # senão, se a opção for = 9, volte para o menu principal
    elif opcao == "9":
        print("Você escolheu sair!")
        break
    else:
        print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")