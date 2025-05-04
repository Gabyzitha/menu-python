# Aluna: Gabrielly Soares Alcântara Mota
# Curso: Análise e desenvolvimento de sistemas

import json

def mostrar_menu_principal():
    print("----- [MENU PRINCIPAL] -----\n")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.\n")

def mostrar_menu_operacoes():
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Editar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.\n")


# funções criar arquvivo e ler arquivo JSON
def salvar_arquivo(nome_arquivo, lista_pessoas):
     with open(nome_arquivo, "w", encoding='utf-8') as arquivo_aberto:
          json.dump(lista_pessoas, arquivo_aberto, ensure_ascii=False, indent=4)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo_aberto:
            lista_pessoas = json.load(arquivo_aberto)

        return lista_pessoas
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo '{nome_arquivo}'.")
        return []


# função geral de listar
def listar(nome_arquivo):
    if nome_arquivo in ["estudantes.json", "professores.json", "disciplinas.json"]:
        _listar_cadastro_padrao(nome_arquivo)
    elif nome_arquivo == "turmas.json":
        _listar_turmas("turmas.json", "professores.json", "disciplinas.json")
    elif nome_arquivo == "matriculas.json":
        _listar_matriculas("matriculas.json", "turmas.json", "estudantes.json")

# subfunções para melhor orgamização da função LISTAR

def _listar_cadastro_padrao(nome_arquivo):
    """Função para listar cadastro padrão (estudantes, professores e disciplinas)"""

    lista_pessoas = ler_arquivo(nome_arquivo)
    print("=========== LISTA ===========\n")
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

def _listar_turmas(nome_arquivo_turma, nome_arquivo_professor, nome_arquivo_disciplina):

    turmas = ler_arquivo(nome_arquivo_turma)
    professores = ler_arquivo(nome_arquivo_professor)
    disciplinas = ler_arquivo(nome_arquivo_disciplina)

    print("=========== LISTA ===========\n")
    # se a lista estiver vazia, informe ao usuário
    if not turmas:
        print("Não há nenhuma turma cadastrada no momento!.\n")
        print("=" * 29)
        return

    # senão, exibir a lista
    print("Lista de Cadastros:\n")

    #a função next() vai retornar o primeiro prof/disc encontrado com o código igual o da turma
    for turma in turmas:
        prof = next((p for p in professores if p["código"] == turma["codigo_professor"]), {})
        disc = next((d for d in disciplinas if d["código"] == turma["codigo_disciplina"]), {})

        print(f"Código: {turma['codigo_turma']}")
        print(f"Professor: {prof.get('código', 'Não Encontrado!')} - {prof.get('nome', 'Não Encontrado!')}")
        print(f"Disciplina: {disc.get('código', 'Não Encontrado!')} - {disc.get('nome', 'Não Encontrado!')}")
        print("-" * 40)

def _listar_matriculas(nome_arquivo_matricula, nome_arquivo_turma, nome_arquivo_estudante):

    matriculas = ler_arquivo(nome_arquivo_matricula)
    turmas = ler_arquivo(nome_arquivo_turma)
    estudantes = ler_arquivo(nome_arquivo_estudante)

    print("=========== LISTA ===========\n")
    # se a lista estiver vazia, informe ao usuário
    if not matriculas:
        print("Não há nenhuma matrícula cadastrada no momento!.\n")
        print("=" * 29)
        return

    # senão, exibir a lista
    print("Lista de Cadastros:\n")

    #a função next() vai retornar o primeira turma/estudante encontrado com o código igual o da matricula
    for matricula in matriculas:
        turma = next((t for t in turmas if t["codigo_turma"] == matricula["codigo_turma"]), {})
        estudante = next((e for e in estudantes if e["código"] == matricula["codigo_estudante"]), {})

        print(f"Código: {matricula['codigo_matricula']}")
        print(f"Turma: {turma.get('codigo_turma', 'Não Encontrado!')}")
        print(f"Estudante: {estudante.get('código', 'Não Encontrado!')} - {estudante.get('nome', 'Não Encontrado!')} - "
              f" CPF: {estudante.get('cpf', 'Não Encontrado!')}")

        print("-" * 40)



# função geral para editar
def editar(nome_arquivo):

    lista = ler_arquivo(nome_arquivo)
    print("=========== EDITAR ===========\n")

    try:
        codigo_editar = int(input("Informe o código que deseja editar: "))

        # se for matrícula
        if nome_arquivo == "matriculas.json":
           _editar_matriculas(nome_arquivo, lista, codigo_editar)

        # se for turma
        elif nome_arquivo == "turmas.json":
            _editar_turma(nome_arquivo, lista, codigo_editar)

        # se for estudantes/prof/disciplina
        else:
          _editar_cadastro_padrao(nome_arquivo, lista, codigo_editar)

    except ValueError:
        print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")

# subfunções para melhor organização da função EDITAR

def _editar_cadastro_padrao(nome_arquivo,lista, codigo_editar):
    """Edita campos padrão de cadastro (código, nome, cpf)."""

    editar_cadastro = None
    for item in lista:
        if item["código"] == codigo_editar:
            editar_cadastro = item
            print("Por favor, digite as novas informações de cadastro!\n")
            editar_cadastro["código"] = int(input("\nInforme o novo código: "))
            editar_cadastro["nome"] = input("Informe o novo nome: ")
            if "cpf" in editar_cadastro:
                editar_cadastro["cpf"] = input("Informe o novo CPF: ")
            print("\nEdição feita com sucesso!\n")
            salvar_arquivo(nome_arquivo, lista)
            break

    if editar_cadastro is None:
        print(f"Não encontramos a pessoa de código: {codigo_editar}.\n")
    print("=" * 29)

def _editar_turma(nome_arquivo, lista, codigo_editar):
    """Edita informações específicas de uma turma."""

    turma_encontrada = None
    for turma in lista:
        if turma["codigo_turma"] == codigo_editar:
            turma_encontrada = turma
            break
    if not turma_encontrada:
        print(f"Não encontramos nenhuma turma com código: {codigo_editar}.\n")
        return

    professores = ler_arquivo("professores.json")
    disciplinas = ler_arquivo("disciplinas.json")

    # editar professor
    novo_prof = int(input("Informe o novo código do professor: "))
    professor_existe = False
    for professor in professores:
        if professor["código"] == novo_prof:
            professor_existe = True
            break
    if not professor_existe:
        print("Não existe um professor de código: ", novo_prof, "cadastrado, tente novamente! \n")
        return

    # editar disciplina
    nova_disc = int(input("Informe o novo código da disciplina: "))
    disciplina_existe = False
    for disciplina in disciplinas:
        if disciplina["código"] == nova_disc:
            disciplina_existe = True
            break
    if not disciplina_existe:
        print("Não existe uma disciplina de código: ", nova_disc, "cadastrado, tente novamente! \n")
        return

    turma_encontrada["codigo_professor"] = novo_prof
    turma_encontrada["codigo_disciplina"] = nova_disc

    salvar_arquivo(nome_arquivo, lista)
    print("Cadastro Editado com sucesso! \n")

def _editar_matriculas(nome_arquivo, lista, codigo_editar):
    """Edita informações específicas de uma matrícula."""

    matricula_encontrada = None
    for matricula in lista:
        if matricula["codigo_matricula"] == codigo_editar:
            matricula_encontrada = matricula
            break
    if not matricula_encontrada:
        print(f"Não encontramos nenhuma matrícula com código: {codigo_editar}.\n")
        return

    turmas = ler_arquivo("turmas.json")
    estudantes = ler_arquivo("estudantes.json")

    # editar turma
    nova_turma = int(input("Informe o novo código da turma: "))
    turma_existe = False
    for turma in turmas:
        if turma["codigo_turma"] == nova_turma:
            turma_existe = True
            break
    if not turma_existe:
        print("Não existe um professor de código: ", nova_turma, "cadastrado, tente novamente! \n")
        return

    # editar estudante
    novo_estudante = int(input("Informe o novo código do estudante: "))
    estudante_existe = False
    for estudante in estudantes:
        if estudante["código"] == novo_estudante:
            estudante_existe = True
            break
    if not estudante_existe:
        print("Não existe nenhum estudante de código: ", novo_estudante, "cadastrado, tente novamente! \n")
        return

    matricula_encontrada["codigo_turma"] = nova_turma
    matricula_encontrada["codigo_estudante"] = novo_estudante

    salvar_arquivo(nome_arquivo, lista)
    print("Cadastro Editado com sucesso! \n")



# função geral para excluir
def excluir(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    print("=========== EXCLUIR ===========\n")

    try:
        codigo_excluir = int(input("Informe o código que deseja excluir: "))

        # se for matrícula
        if nome_arquivo == "matriculas.json":
          _excluir_matricula(nome_arquivo, lista, codigo_excluir)

        # se for turma
        elif nome_arquivo == "turmas.json":
          _excluir_turma(nome_arquivo, lista, codigo_excluir)

        # remover estudante, professor ou disciplina
        else:
           _excluir_cadastro_padrao(nome_arquivo, lista, codigo_excluir)

        print("=" * 29)
    except ValueError:
        print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")

# subfunções para melhor organização da função EXCLUIR

def _excluir_cadastro_padrao(nome_arquivo, lista, codigo_excluir):
    """Função para excluir cadastros padrão (estudantes, professores e disciplinas"""

    remover_cadastro = None
    for item in lista:
        if item["código"] == codigo_excluir:
            remover_cadastro = item
            break

    if remover_cadastro:
        lista.remove(remover_cadastro)
        salvar_arquivo(nome_arquivo, lista)
        print("Cadastro Removido com sucesso! \n")
    else:
        print(f"Não encontramos a pessoa de código: {codigo_excluir}.\n")

def _excluir_turma(nome_arquivo, lista, codigo_excluir):
    """Função para excluir uma turma."""

    remover_turma = None
    for turma in lista:
        if turma["codigo_turma"] == codigo_excluir:
            remover_turma = turma
            break

    if remover_turma:
        lista.remove(remover_turma)
        salvar_arquivo(nome_arquivo, lista)
        print("Cadastro Removido com sucesso! \n")
    else:
        print(f"Não encontramos turma de código: {codigo_excluir}.\n")

def _excluir_matricula(nome_arquivo, lista, codigo_excluir):
    """Função para excluir matrículas"""

    remover_matricula = None
    for matricula in lista:
        if matricula["codigo_matricula"] == codigo_excluir:
            remover_matricula = matricula
            break

    if remover_matricula:
        lista.remove(remover_matricula)
        salvar_arquivo(nome_arquivo, lista)
        print("Cadastro Removido com sucesso! \n")
    else:
        print(f"Não encontramos matrícula de código: {codigo_excluir}.\n")



# função geral de incluir
def incluir(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)

    if nome_arquivo == "estudantes.json":
        _incluir_cadastro_padrao(nome_arquivo, lista, incluir_cpf=True)
    elif nome_arquivo == "professores.json":
        _incluir_cadastro_padrao(nome_arquivo, lista, incluir_cpf=True)
    elif nome_arquivo == "disciplinas.json":
        _incluir_cadastro_padrao(nome_arquivo, lista, incluir_cpf=False)
    elif nome_arquivo == "turmas.json":
        _incluir_turmas("turmas.json", "professores.json", "disciplinas.json")
    elif nome_arquivo == "matriculas.json":
        _incluir_matriculas("matriculas.json", "turmas.json", "estudantes.json")

# subfunções para melhor organização do Incluir
def _incluir_cadastro_padrao(nome_arquivo, lista, incluir_cpf=False):
    """Função para incluir cadastros padrão (estudantes, professores e disciplinas)"""

    print("============== INCLUIR ==============")
    lista = ler_arquivo(nome_arquivo)
    while True:
        # pede o código, nome cpf ao usuário
        try:
            codigo = int(input("\nInforme o código: "))
            nome = input("Informe o nome: ")

            # coloca essas informações em um dicionário
            pessoa_cadastrada = {"código": codigo, "nome": nome}

            if incluir_cpf:
                cpf = input("Informe o CPF: ")
                pessoa_cadastrada["cpf"] = cpf

            for pessoa in lista:
                if pessoa["código"] == codigo:
                    print("Código já cadastrado, tente novamente! \n")
                    break

            # atualiza a lista lendo o arquivo
            lista = ler_arquivo(nome_arquivo)

            # adicona a pessoa na lista
            lista.append(pessoa_cadastrada)

            # salva a lista atualizada
            salvar_arquivo(nome_arquivo, lista)
            print("\n Cadastro feito com sucesso!\n")

            # se a resposta for = "n" volte para o menu de operações
            if input("Deseja cadastrar outro(a) (s/n)? ") == "n":
                break

        except ValueError:
            print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")

    print("Pressione ENTER para continuar.\n")
    print("=" * 36)

def _incluir_turmas(nome_arquivo_turma, nome_arquivo_professor, nome_arquivo_disciplina):
    """Função para incluir turmas"""

    print("============== INCLUIR ==============")

    turmas = ler_arquivo(nome_arquivo_turma)
    professores = ler_arquivo(nome_arquivo_professor)
    disciplinas = ler_arquivo(nome_arquivo_disciplina)

    while True:

        try:
            # pede o código da turma que deseja incluir
            codigo_turma = int(input("\nInforme o código da turma: "))

            # se a turma já existe, recebe uma mensagem de aviso
            existe = False
            for turma in turmas:
                if turma["codigo_turma"] == codigo_turma:
                    existe = True
                    print("Já existe uma turma de código: ", codigo_turma, "cadastrada, tente novamente! \n")
                    break

            # se o professor existe, inclui. Se não, recebe uma mensagem de aviso
            professor_existe = False
            codigo_professor = int(input("Informe o código do professor: "))
            for professor in professores:
                if professor["código"] == codigo_professor:
                    professor_existe = True
                    break
            if not professor_existe:
                print("Não existe um professor de código: ", codigo_professor, "cadastrado, tente novamente! \n")

            # se a disciplina existe, incluir. Se não, recebe uma mensagem de aviso
            disciplina_existe = False
            codigo_disciplina = int(input("Informe o código da disciplina: "))
            for disciplina in disciplinas:
                if disciplina["código"] == codigo_disciplina:
                    disciplina_existe = True
                    break
            if not disciplina_existe:
                print("Não existe uma disciplina de código: ", codigo_disciplina, "cadastrado, tente novamente! \n")

            # informações vão para o dicionário
            turma = {
                "codigo_turma": codigo_turma,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
            }

            # o dicionário vai para lista que vai para o arquivo JSON
            turmas.append(turma)
            salvar_arquivo(nome_arquivo_turma, turmas)
            print("\n Cadastro feito com sucesso!\n")


            # se a resposta for = "n" volte para o menu de operações
            if input("Deseja cadastrar uma nova turma (s/n)? ") == "n":
                break

        except ValueError:
            print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")

    print("Pressione ENTER para continuar.\n")
    print("=" * 36)

def _incluir_matriculas(nome_arquivo_matricula, nome_arquivo_turma, nome_arquivo_estudante):
    """Função para incluir matriculas"""
    print("============== INCLUIR ==============")

    matriculas = ler_arquivo(nome_arquivo_matricula)
    turmas = ler_arquivo(nome_arquivo_turma)
    estudantes = ler_arquivo(nome_arquivo_estudante)


    while True:
        try:
            # pede o código da matrícula que deseja incluir
            codigo_matricula = int(input("\nInforme o código da matrícula: "))

            # se a matrícula não existe, inclui. Se não, recebe mensagem informando
            existe = False
            for matricula in matriculas:
                if matricula["codigo_matricula"] == codigo_matricula:
                    existe = True
                    print("Já existe uma matrícula de código: ", codigo_matricula, "cadastrada, tente novamente! \n")
                    break

            # se a turma existe, inclui. Se não, recebe mensagem informando
            turma_existe = False
            codigo_turma = int(input("Informe o código da turma: "))
            for turma in turmas:
                if turma["codigo_turma"] == codigo_turma:
                    turma_existe = True
                    break
            if not turma_existe:
                print("Não existe uma turma de código: ", codigo_turma, "cadastrado, tente novamente! \n")

            # se o estudante existe, inclui. Se não, recebe mensagem informando
            estudante_existe = False
            codigo_estudante = int(input("Informe o código do estudante: "))
            for estudante in estudantes:
                if estudante["código"] == codigo_estudante:
                    estudante_existe = True
                    break
            if not estudante_existe:
                print("Não existe uma disciplina de código: ", codigo_estudante, "cadastrado, tente novamente! \n")

            # informações vão para o dicionário
            matricula = {
                "codigo_matricula": codigo_matricula,
                "codigo_turma": codigo_turma,
                "codigo_estudante": codigo_estudante
            }

            # dicionário vai para a lista que vai para o arquivo JSON
            matriculas.append(matricula)
            salvar_arquivo(nome_arquivo_matricula, matriculas)
            print("\n Cadastro feito com sucesso!\n")

            # se a resposta for = "n" volte para o menu de operações
            if input("Deseja cadastrar uma nova matrícula (s/n)? ") == "n":
                break

        except ValueError:
            print(" ✖ Apenas números inteiros são considerados, tente novamente! \n")

    print("Pressione ENTER para continuar.\n")
    print("=" * 36)



# função que abrange todas as funcionalidades do menu de operações
def funcionalidades_menu_operacoes(nome_arquivo, opcao2, incluir_cpf=True):
    # se for opção 1, peça para que inclua alunos na lista
    if opcao2 == "1":
        lista_pessoas = ler_arquivo(nome_arquivo)
        incluir(nome_arquivo)

    # se for opção 2, exibir a lista de alunos
    elif opcao2 == "2":
        listar(nome_arquivo)

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

def funcionalidades_menu_operacoes_turmas(nome_arquivo_turma, nome_arquivo_professor, nome_arquivo_disciplina, opcao2):
    if opcao2 == "1":
        incluir(nome_arquivo_turma)

    elif opcao2 == "2":
        listar(nome_arquivo_turma)

    elif opcao2 == "3":
        editar("turmas.json")


    elif opcao2 == "4":
        excluir(nome_arquivo_turma)


    elif opcao2 == "9":
        print("Você escolheu voltar para o [MENU PRINCIPAL]\n")
        return False

    else:
        print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")

    return True

def funcionalidades_menu_operacoes_matriculas(nome_arquivo_matricula, nome_arquivo_turma, nome_arquivo_estudante, opcao2):
    if opcao2 == "1":
        incluir(nome_arquivo_matricula)
    elif opcao2 == "2":
        listar(nome_arquivo_matricula)

    elif opcao2 == "3":
        editar("matriculas.json")


    elif opcao2 == "4":
        excluir(nome_arquivo_matricula)


    elif opcao2 == "9":
        print("Você escolheu voltar para o [MENU PRINCIPAL]\n")
        return False

    else:
        print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")

    return True

# menus
def menu_estudantes():
    nome_arquivo = "estudantes.json"
    while True:
        print(f"★★★★★ [ESTUDANTES] MENU DE OPERAÇÕES ★★★★★\n")
        mostrar_menu_operacoes()

        # coletando a opção2
        opcao2 = input("Informe a opção desejada: ")
        print(f"Você escolheu a opção válida ({opcao2})\n")
        continuar = funcionalidades_menu_operacoes(nome_arquivo, opcao2, incluir_cpf=True)
        if not continuar:
            break

def menu_professores():
    nome_arquivo = "professores.json"
    while True:
        print(f"★★★★★ [PROFESSORES] MENU DE OPERAÇÕES ★★★★★\n")
        mostrar_menu_operacoes()

        # coletando a opção2
        opcao2 = input("Informe a opção desejada: ")
        print(f"Você escolheu a opção válida ({opcao2})\n")
        continuar = funcionalidades_menu_operacoes(nome_arquivo, opcao2, incluir_cpf=True)
        if not continuar:
            break

def menu_disciplinas():
    nome_arquivo = "disciplinas.json"
    while True:
        print(f"★★★★★ [DISCIPLINAS] MENU DE OPERAÇÕES ★★★★★\n")
        mostrar_menu_operacoes()

        # coletando a opção2
        opcao2 = input("Informe a opção desejada: ")
        print(f"Você escolheu a opção válida ({opcao2})\n")
        continuar = funcionalidades_menu_operacoes(nome_arquivo, opcao2, incluir_cpf=False)
        if not continuar:
            break

def menu_turmas():
    nome_arquivo = "turmas.json"
    nome_arquivo_professor = "professores.json"
    nome_arquivo_disciplina = "disciplinas.json"
    nome_arquivo_turma = "turmas.json"

    while True:
        print(f"★★★★★ [TURMAS] MENU DE OPERAÇÕES ★★★★★\n")
        mostrar_menu_operacoes()

        # coletando a opção2
        opcao2 = input("Informe a opção desejada: ")
        print(f"Você escolheu a opção válida ({opcao2})\n")
        continuar = funcionalidades_menu_operacoes_turmas(nome_arquivo_turma, nome_arquivo_professor, nome_arquivo_disciplina, opcao2)
        if not continuar:
            break

def menu_matriculas():
    nome_arquivo = "matriculas.json"
    nome_arquivo_matricula = "matriculas.json"
    nome_arquivo_turma = "turmas.json"
    nome_arquivo_estudante = "estudantes.json"

    while True:
        print(f"★★★★★ [MATRÍCULAS] MENU DE OPERAÇÕES ★★★★★\n")
        mostrar_menu_operacoes()

        # coletando a opção2
        opcao2 = input("Informe a opção desejada: ")
        print(f"Você escolheu a opção válida ({opcao2})\n")
        continuar = funcionalidades_menu_operacoes_matriculas(nome_arquivo_matricula, nome_arquivo_turma, nome_arquivo_estudante, opcao2)
        if not continuar:
            break


# mostre o menu principal enquanto o usuário n decidir sair
while True:
    # menu principal
    mostrar_menu_principal()

    # coletando opção 1
    opcao = input("Informe a opção desejada: ")
    print(f"Você escolheu a opção válida ({opcao})\n")

    if opcao == "1":
        menu_estudantes()

    elif opcao == "2":
        menu_professores()

    elif opcao == "3":
        menu_disciplinas()

    elif opcao == "4":
        menu_turmas()

    # senão, se for uma dessas opções, informe que está em desenvolvimento
    elif opcao == "5":
        menu_matriculas()

    # senão, se a opção for = 9, volte para o menu principal
    elif opcao == "9":
        print("Você escolheu sair!")
        break
    else:
        print("Você escolheu uma opção INVÁLIDA, tente novamente!\n")