# Aluna: Gabrielly Soares Alcântara Mota
# Curso: Análise e desenvolvimento de sistemas


# lista de estudantes vazia para coletar informações
lista_estudantes = []

# mostre o menu principal enquanto o usuário n decidir sair
while True:
    # menu principal
    print("----- [MENU PRINCIPAL] -----\n")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.\n")

    # coletando a opção 1
    opcao = input("Informe a opção desejada: ")

    # se a opção for 1, mostre o menu de operações enquanto o usuário não decidir sair
    if opcao == "1":
        while True:
            print(f"Você escolheu a opção válida ({opcao})\n")

            # menu de operações
            print(f"★★★★★ [ESTUDANTES] MENU DE OPERAÇÕES ★★★★★\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Editar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.\n")

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print(f"Você escolheu a opção válida ({opcao2})\n")

            # se for opção 1, peça para que inclua alunos na lista
            if opcao2 == "1":
                print("=========== INCLUIR ===========")

                # pedir código,nome e cpf ao usuário enquanto o usuário não decidir sair
                while True:
                    codigo = int(input("\nInforme o código do estudante: "))
                    nome = input("Informe o nome do estudante: ")
                    cpf = input("Informe o CPF do estudante: ")

                    # coloca essas informações em um dicionário
                    dados_estudante = {"código": codigo, "nome": nome, "cpf": cpf}
                    # coloca esse dicionário na lista_estudantes
                    lista_estudantes.append(dados_estudante)
                    print("\nEstudante cadastrado com sucesso!\n")

                    #se a resposta for = "n" volte para o menu de operações
                    if input("Deseja cadastrar um novo contato (s/n)? ") == "n":
                        break

                print("Pressione ENTER para continuar.\n")
                print("=" * 30)


            # se for opção 2, exibir a lista de alunos
            elif opcao2 == "2":
                print("=========== LISTA ===========\n")
                # se a lista de estudantes estiver vazia, informe ao usuário
                if len(lista_estudantes) == 0:
                    print("Não há estudantes cadastrados.\n")
                    print("=" * 29)
                # senão, exibir a lista
                else:
                    print("Lista de Estudantes:\n")
                    for i, dados in enumerate(lista_estudantes):
                        print(dados)
                    print("Pressione ENTER para continuar.\n")
                    print("=" * 29)

            elif opcao2 == "3":
                print("=========== EDITAR ===========\n")

                #coletando o código do estudante no qual o usuário deseja editar
                codigo_editar = int(input("Informe o código do estudante que deseja editar: "))

                editar_estudante = None

                for dados_estudante in lista_estudantes:
                    if dados_estudante["código"] == codigo_editar:
                        editar_estudante = dados_estudante
                        print("Por favor, edite os dados do estudante!\n")
                        editar_estudante["código"] = int(input("\nInforme o novo código do estudante: "))
                        editar_estudante["nome"] = input("Informe o novo nome do estudante: ")
                        editar_estudante["cpf"] = input("Informe o novo CPF do estudante: ")
                        print("\nEstudante editado com sucesso!\n")
                        break
                    elif editar_estudante is None:
                        print(f"Não encontramos o estudante de código: {codigo_editar}.\n")
                print("=" * 29)

             # se for opção 4, exibir a sessão de excluir
            elif opcao2 == "4":
                print("=========== EXCLUIR ===========\n")

                # coletando o código do estudante no qual o usuário deseja excluir
                codigo_excluir = int(input("Informe o código do estudante que deseja excluir: "))

                remover_estudante = None
                for dados_estudante in lista_estudantes:
                   if dados_estudante["código"] == codigo_excluir:
                      remover_estudante = dados_estudante
                      lista_estudantes.remove(remover_estudante)
                      print(" Estudante removido com sucesso!\n")
                      break
                   elif remover_estudante is None:
                       print(f"Não encontramos o estudante de código: {codigo_excluir}.\n")
                print("=" * 29)


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