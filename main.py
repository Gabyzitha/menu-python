# Aluna: Gabrielly Soares Alcântara Mota
# Curso: Análise e desenvolvimento de sistemas

import json
from traceback import print_tb

# lista de pessoas vazia para coletar informações
lista_pessoas = []
lista_de_turmas = []

def em_desenvolvimento():
    print("=" * 25)
    print("\n    EM DESENVOLVIMENTO\n")
    print("=" * 25)


# função para exibir o menu principal
def mostrar_menu_principal():
    print("----- [MENU PRINCIPAL] -----\n")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.\n")


# função para exibir o menu de operações
def mostrar_menu_operacoes():
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Editar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.\n")


def obter_dados_pessoa(incluir_cpf):
    codigo = int(input("\nInforme o código: "))
    nome = input("Informe o nome: ")
    pessoa_cadastrada = {"código": codigo , "nome": nome}

    if incluir_cpf:
      cpf = input("Informe o CPF: ")
      pessoa_cadastrada["cpf"] = cpf

    return pessoa_cadastrada

def obter_dados_turma():
    codigo_turma = int(input("Informe o código da turma: "))
    codigo_professor = int(input("Informe o código do professor: "))
    codigo_disciplina = int(input("Informe o código da disciplina: "))
    turma_cadastrada = {
        "Código da turma": codigo_turma,
        "Código do professor": codigo_professor,
        "Código da disciplina": codigo_disciplina
    }
    return turma_cadastrada

# função de incluir código, nome e cpf
def incluir(nome_arquivo, lista_pessoas, pessoa_cadastrada=True, incluir_cpf=True):
    print("============== INCLUIR ==============")
    while True:
        # pede o código, nome cpf ao usuário
       try:
           if pessoa_cadastrada:
               pessoa_cadastrada = obter_dados_pessoa(incluir_cpf)
               #atualiza a lista lendo o arquivo
               lista_pessoas = ler_arquivo(nome_arquivo)
               # adicona a pessoa na lista
               lista_pessoas.append(pessoa_cadastrada)
               #salva lista atualizada
               salvar_arquivo(nome_arquivo, lista_pessoas)

           else:
               turma_cadastrada = obter_dados_turma()
               lista_de_turmas = ler_arquivo(nome_arquivo)
               lista_de_turmas.append(turma_cadastrada)
               # salva a lista atualizada
               salvar_arquivo(nome_arquivo, lista_de_turmas)
               print("\n Cadastro feito com sucesso!\n")

           # se a resposta for = "n" volte para o menu de operações
           if input("Deseja cadastrar uma nova pessoa (s/n)? ") == "n":
                break

       except ValueError:
         print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")


    print("Pressione ENTER para continuar.\n")
    print("=" * 36)


# função para exibir a lista
def listar(nome_arquivo, pessoa_cadastrada=True):


        print("=========== LISTA ===========\n")

        if pessoa_cadastrada == True:
            lista_pessoas = ler_arquivo(nome_arquivo)
            # se a lista estiver vazia, informe ao usuário
            if len(lista_pessoas) == 0:
                print("Não há ninguém cadastrado no momento!.\n")
                print("=" * 29)
            # senão, exibir a lista
            else:
                print("Lista de Cadastros:\n")
                for dados in lista_pessoas:
                    print(f"Código: {dados['código']}")
                    print(f"Nome: {dados['nome']}")
                    if "cpf" in dados:
                        print(f"CPF: {dados['cpf']}")
                    print("-" * 30)
        else:
            lista_de_turmas = ler_arquivo(nome_arquivo)
            if len(lista_de_turmas) == 0:
                print("Não há nenhuma turma cadastrada no momento!.\n")
                print("=" * 29)
            else:
                print("Lista de Turmas:\n")
                professores = ler_arquivo("professores.json")
                disciplinas = ler_arquivo("disciplinas.json")



                for turma in lista_de_turmas:
                    if turma is not None:
                        print(f"Código da Turma: {turma['Código da turma']} ")
                        print(f"Professor: {turma['Código do professor']} ")
                        print(f"Código da Disciplina: {turma['Código da disciplina']} ")
                        print("-" * 30)


# função para editar o cadastro
def editar(nome_arquivo):
    lista_pessoas = ler_arquivo(nome_arquivo)
    print("=========== EDITAR ===========\n")

    try:

        # coletando o código da pessoa no qual o usuário deseja editar
        codigo_editar = int(input("Informe o código da pessoa que deseja editar: "))

        editar_cadastro = None

        for pessoa_cadastrada in lista_pessoas:
            if pessoa_cadastrada["código"] == codigo_editar:
                editar_cadastro = pessoa_cadastrada
                print("Por favor, digite as novas informações de cadastro!\n")
                editar_cadastro["código"] = int(input("\nInforme o novo código: "))
                editar_cadastro["nome"] = input("Informe o novo nome: ")
                if "cpf" in editar_cadastro:
                    editar_cadastro["cpf"] = input("Informe o novo CPF: ")
                print("\nEdição feita com sucesso!\n")
                salvar_arquivo(nome_arquivo, lista_pessoas)
                break

        if editar_cadastro is None:
            print(f"Não encontramos a pessoa de código: {codigo_editar}.\n")
        print("=" * 29)
    except ValueError:
        print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")


# função de excluir
def excluir(nome_arquivo):
    lista_pessoas = ler_arquivo(nome_arquivo)
    print("=========== EXCLUIR ===========\n")

    try:
        # coletando o código da pessoa no qual o usuário deseja excluir
        codigo_excluir = int(input("Informe o código da pessoa que deseja excluir: "))

        remover_cadastro = None
        for pessoa_cadastrada in lista_pessoas:
            if pessoa_cadastrada["código"] == codigo_excluir:
                remover_cadastro = pessoa_cadastrada
                break

        if remover_cadastro:
            lista_pessoas.remove(remover_cadastro)
            salvar_arquivo(nome_arquivo, lista_pessoas)
            print("Cadastro Removido com sucesso! \n")
        else:
            print(f"Não encontramos a pessoa de código: {codigo_excluir}.\n")

        print("=" * 29)
    except ValueError:
        print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")


# função criar arquvivo JSON
def salvar_arquivo(nome_arquivo, lista_pessoas):
     with open(nome_arquivo, "w", encoding='utf-8') as arquivo_aberto:
          json.dump(lista_pessoas, arquivo_aberto, ensure_ascii=False, indent=4)


# função ler arquivo JSON
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo_aberto:
            lista_pessoas = json.load(arquivo_aberto)

        return lista_pessoas
    except:
        return []


# função que abrange todas as funcionalidades do menu de operações
def funcionalidades_menu_opercoes(nome_arquivo, lista_pessoas, opcao2, pessoa_cadastrada=True, incluir_cpf=True):
    # se for opção 1, peça para que inclua alunos na lista
    if opcao2 == "1":
        incluir(nome_arquivo, lista_pessoas, pessoa_cadastrada, incluir_cpf)

    # se for opção 2, exibir a lista de alunos
    elif opcao2 == "2":
        listar(nome_arquivo, pessoa_cadastrada)

    elif opcao2 == "3":
        editar(nome_arquivo)

    # se for opção 4, exibir a sessão de excluir
    elif opcao2 == "4":
        excluir(nome_arquivo)

    # senão, se a opção for = 9, volte para o menu principal
    elif opcao2 == "9":
        print("Você escolheu voltar para o [MENU PRINCIPAL]\n")
        return False
    # senão for nenhuma dessas, considere inválida
    else:
        print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")

    return True




# mostre o menu principal enquanto o usuário n decidir sair
while True:
    # menu principal
    mostrar_menu_principal()

    # coletando opção 1
    opcao = input("Informe a opção desejada: ")
    print(f"Você escolheu a opção válida ({opcao})\n")

    # se a opção for 1, mostre o menu de operações enquanto o usuário não decidir sair
    if opcao == "1":
        nome_arquivo = "estudantes.json"
        while True:


            # menu de operações
            print(f"★★★★★ [ESTUDANTES] MENU DE OPERAÇÕES ★★★★★\n")
            mostrar_menu_operacoes()

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print(f"Você escolheu a opção válida ({opcao2})\n")
            continuar = funcionalidades_menu_opercoes(nome_arquivo, lista_pessoas, opcao2, incluir_cpf=True)
            if not continuar:
                break

    elif opcao == "2":
        nome_arquivo = "professores.json"
        while True:

            # menu de operações
            print(f"★★★★★ [PROFESSORES] MENU DE OPERAÇÕES ★★★★★\n")
            mostrar_menu_operacoes()

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print(f"Você escolheu a opção válida ({opcao2})\n")
            continuar = funcionalidades_menu_opercoes(nome_arquivo, lista_pessoas, opcao2, incluir_cpf=True)
            if not continuar:
                break

    # senão, se for uma dessas opções, informe que está em desenvolvimento

    elif opcao == "3":
        nome_arquivo = "disciplinas.json"
        while True:

            # menu de operações
            print(f"★★★★★ [DISCIPLINAS] MENU DE OPERAÇÕES ★★★★★\n")
            mostrar_menu_operacoes()

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print(f"Você escolheu a opção válida ({opcao2})\n")
            continuar = funcionalidades_menu_opercoes(nome_arquivo, lista_pessoas, opcao2, incluir_cpf=False)
            if not continuar:
                break

    elif opcao == "4":
        nome_arquivo = "turmas.json"
        while True:

            # menu de operações
            print(f"★★★★★ [TURMAS] MENU DE OPERAÇÕES ★★★★★\n")
            mostrar_menu_operacoes()

            # coletando a opção2
            opcao2 = input("Informe a opção desejada: ")
            print(f"Você escolheu a opção válida ({opcao2})\n")
            continuar = funcionalidades_menu_opercoes(nome_arquivo, lista_pessoas, opcao2, pessoa_cadastrada=False, incluir_cpf=False)
            if not continuar:
                break


    elif opcao == "5":
        em_desenvolvimento()

    # senão, se a opção for = 9, volte para o menu principal
    elif opcao == "9":
        print("Você escolheu sair!")
        break
    else:
        print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")