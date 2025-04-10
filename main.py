# Aluna: Gabrielly Soares Alcântara Mota
# Curso: Análise e desenvolvimento de sistemas


# lista de estudantes vazia para coletar informações
# enquanto for verdade mostre o menu principal
while True:
    # menu principal
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")

    # coletando a opção
    opcao = input("Informe a opção desejada: ")

    # se a opção for 1, mostre o menu de operações enquanto for verdade
    if opcao == "1":
        while True:

            # mostrando o menu de operações
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")

            # se for opção 1, peça para que inclua alunos na lista
            if opcao2 == "1":
                print("=========== INCLUIR ===========")
                    nome = input("Informe o nome do estudante: ")
                print("=" * 30)

                # colocar o "nome" na listaEstudantes

            # se for opção 2, exiba a lista de alunos
            elif opcao2 == "2":
                # se a lista de estudantes estiver vazia, informe ao usuário
                    print("=" * 29)
                # senão, exibir a lista
                else:
                    print("=" * 29)


            # senão, se for uma dessas opções, mostre que está em desenvolvimento
            elif opcao2 == "3" or opcao2 == "4":
                # mostrando que está em desenvlvimento
                print("=" * 25)

            # senão, se a opção for = 9, volte para o menu principal
            elif opcao2 == "9":
                break
            # senão for nenhuma dessas, considere inválida
            else:

    # senão, se for uma dessas opções, informe que está em desenvolvimento
    elif opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        print("=" * 25)

    # senão, se a opção for = 9, volte para o menu principal
    elif opcao == "9":
        print("Você escolheu sair!")
        break
    else: