# Lista principal (Raiz) onde cada currículo será armazenado como uma lista
curriculos = []  # Inicializa uma lista vazia para armazenar os currículos.

# Função para formatar o nome (remover espaços extras e colocar em formato título)
def formatar_nome(nome):
    return nome.strip().title()  # Remove espaços extras e coloca a string em formato título.

# Função para cadastrar um novo currículo
def cadastrar_curriculo():
    print("\n=== Cadastro de Currículo ===")  # Exibe um 'titulo' na página de cadastro.
    
    nome = input("Nome completo: ").strip()  # Solicita o nome do usuário e o strip remove espaços extras.
    while not nome:  # Enquanto o nome não possuir um valor, solicita novamente.
        print("Nome não pode ser vazio.")
        nome = input("Nome completo: ").strip()
    nome = formatar_nome(nome)  # Formata o nome.

    idade = input("Idade: ").strip()  # Solicita a idade do usuário.
    while not idade.isdigit() or int(idade) <= 0:  # Verifica se a idade é um número inteiro positivo.
        print("A idade deve ser um número inteiro positivo.")
        idade = input("Idade: ").strip()
    idade = int(idade)  # Converte a idade para inteiro.

    formacao = input("Formação acadêmica: ").strip()  # Solicita a formação acadêmica.
    while not formacao:
        print('Você precisa colocar ao menos 1 formação')
        formacao = input("Formação acadêmica: ").strip()

    print("Digite as experiências profissionais (cargo, empresa e tempo de vigência). Digite 'fim' para encerrar:")
    experiencias = []  # Inicializa uma lista para armazenar as experiências profissionais.
    while True:  # Enquanto o loop tiver um valor verdadeiro: ...
        exp = input("- ").strip()  # Solicita a experiência.
        if exp.lower() == "fim":  # Se o usuário digitar "fim", encerra o loop.
            if len(experiencias) == 0:  # Verifica se pelo menos um item foi adicionado na lista 'experiência'.
                print("É necessário ao menos uma experiência.")
            else:
                break
        elif exp:  # Se não estiver vazia, adiciona os inputs que foram enviados para a variável exp na lista.
            experiencias.append(exp)

    print("Digite as habilidades (uma por linha). Digite 'fim' para encerrar:")
    habilidades = []  # Inicializa uma lista para armazenar as habilidades.
    while True:  # Enquanto o loop tiver um valor verdadeiro: ...
        hab = input("- ").strip()  # Solicita uma habilidade.
        if hab.lower() == "fim":  # Se o usuário digitar "fim", encerra o loop.
            break
        elif hab:  # Se não estiver vazia, adiciona os inputs que foram enviados para a variável hab na lista.
            habilidades.append(hab)

    curriculo = [nome, idade, formacao, experiencias, habilidades]  # Cria o currículo como uma lista usando as outras listas como item.
    curriculos.append(curriculo)  # Adiciona o currículo à lista principal.
    print("Currículo cadastrado com sucesso!")  # Confirma o cadastro.

from tabulate import tabulate  # Importa a biblioteca tabulate aprendida na aula do dia 05/05

# Função para listar todos os currículos cadastrados
def listar_curriculos():
    print("\n=== Lista de Currículos ===")  # Exibe o título da seção de listas de currículos.
    if not curriculos:  # Verifica se a lista de currículos está vazia.
        print("Nenhum currículo cadastrado.")  # Exibe mensagem se não houver currículos.
        return

    # Cria uma lista de cabeçalhos e dados para a tabela
    tabela = []
    for i, curr in enumerate(curriculos):
        tabela.append([i + 1, curr[0], curr[1], curr[2], ", ".join(curr[3]), ", ".join(curr[4])])  # Adicionando as informações de nome, formação, idade e etc.. na tabela. 

    # Define os cabeçalhos da tabela
    cabecalhos = ["#", "Nome", "Idade", "Formação", "Experiências", "Habilidades"]

    # Exibe a tabela formatada
    print(tabulate(tabela, headers=cabecalhos, tablefmt="grid"))

# Função para buscar currículos pelo nome
def buscar_curriculo():
    termo = input("\nDigite o nome (ou parte) a buscar: ").strip().lower()  # Solicita o termo de busca.
    encontrados = [c for c in curriculos if termo in c[0].lower()]  # Filtra currículos que contêm o termo no nome.
    if not encontrados:  # Verifica se nenhum currículo foi encontrado.
        print("Nenhum currículo encontrado com esse nome.")
    else:
        for i, curr in enumerate(encontrados):  # percorre sobre os currículos encontrados.
            print(f"\nResultado {i+1}:")  # Exibe o número do resultado.
            print(f" Nome: {curr[0]}")  # Exibe o nome.
            print(f" Idade: {curr[1]}")  # Exibe a idade.
            print(f" Formação: {curr[2]}")  # Exibe a formação acadêmica.
            print(" Experiência:")  # Exibe as experiências profissionais.
            for exp in curr[3]:  # percorre sobre as experiências.
                print(f"  - {exp}")
            print(" Habilidades:")  # Exibe as habilidades.
            for hab in curr[4]:  # percorre sobre as habilidades.
                print(f"  - {hab}")
# Função para selecionar um currículo pela pesquisa
def selecionar_curriculo():
    listar_curriculos()  # Executa a função para Listar todos os currículos.
    if not curriculos:  # Verifica se não há currículos cadastrados.
        return None 
    escolha = input("\nDigite o número do currículo a selecionar: ").strip()  # Solicita o número do currículo, Novamente o .strip() para retirar algum possivel espaço que seja deixado na resposta. 
    if escolha.isdigit():  # Verifica se a entrada é um número.
        indice = int(escolha) - 1  # Converte para índice (base 0).
        if 0 <= indice < len(curriculos):  # Verifica se o indice é maior que a lista curriculos. 
            return indice
    print("Seleção inválida.")  # Exibe mensagem de erro se a seleção for inválida.
    return None

# Função para atualizar algum currículo
def atualizar_curriculo():
    print("\n=== Atualizar Currículo ===")  # Exibe o título da seção de atualizar curriculo.
    indice = selecionar_curriculo()  # Solicita que o usuario escolha um currículo.
    if indice is None:  # Verifica se nenhum currículo foi selecionado. 
        return
    
    curriculo = curriculos[indice]  # Obtém o currículo selecionado.
    print("Pressione ENTER para manter os valores atuais.")  # Instrução para manter valores atuais.

    nome = input(f"Novo nome [{curriculo[0]}]: ").strip()  # Solicita o novo nome.
    if nome:  # Atualiza o nome se fornecido.
        curriculo[0] = formatar_nome(nome)

    idade = input(f"Idade:  [{curriculo[1]}]: ").strip()  # Solicita a nova idade.
    if idade.isdigit() and int(idade) > 0:  # Atualiza a idade se válida.
        curriculo[1] = int(idade)

    formacao = input(f"Nova formação [{curriculo[2]}]: ").strip()  # Solicita a nova formação.
    if formacao:  # Atualiza a formação se fornecida.
        curriculo[2] = formacao

    print("Atualizar experiências? (s para sim// enter para não)")  # Pergunta se deseja atualizar as experiências.
    if input().strip().lower() == 's':  # Se sim, solicita as novas experiências.
        novas_exp = []  # Inicializa uma nova lista de experiências.
        print("Digite as novas experiências. Digite 'fim' para encerrar:")
        while True:
            exp = input("- ").strip()
            if exp.lower() == "fim":  # Encerra o loop ao digitar "fim".
                if novas_exp:  # Atualiza as experiências no currículo.
                    curriculo[3] = novas_exp
                    break
                else:
                    print("É necessário ao menos uma experiência.")
            elif exp:  # Adiciona a experiência à lista.
                novas_exp.append(exp)

    print("Atualizar habilidades? (s para sim)")  # Pergunta se deseja atualizar as habilidades.
    if input().strip().lower() == 's':  # Se sim, solicita as novas habilidades.
        novas_hab = []  # Inicializa uma nova lista de habilidades.
        print("Digite as novas habilidades. Digite 'fim' para encerrar:")
        while True:
            hab = input("- ").strip()
            if hab.lower() == "fim":  # Encerra o loop ao digitar "fim".
                break
            elif hab:  # Adiciona a habilidade à lista.
                novas_hab.append(hab)
        curriculo[4] = novas_hab  # Atualiza as habilidades no currículo.

    print("Currículo atualizado com sucesso!")  # Confirma a atualização.

# Função para excluir um currículo
def excluir_curriculo():
    print("\n=== Excluir Currículo ===")  # Exibe o título da seção de exclusão.
    indice = selecionar_curriculo()  # Solicita a seleção de um currículo.
    if indice is not None:  # Verifica se um currículo foi selecionado.
        curriculos.pop(indice)  # Remove o currículo da lista.
        print("Currículo excluído com sucesso!")  # Confirma a exclusão.

from tabulate import tabulate  # Importa a biblioteca tabulate

# Função principal do menu
def menu():
    while True:  # Loop infinito para exibir o menu até o usuário sair.
        # Define as opções do menu
        opcoes = [
            ["Opção", "Descrição", ""],  # Linha extra para o cabeçalho "MENU"
            ["1", "Cadastrar currículo", ""],
            ["2", "Listar todos os currículos", ""],
            ["3", "Buscar currículo por nome", ""],
            ["4", "Atualizar currículo", ""],
            ["5", "Excluir currículo", ""],
            ["0", "Sair", ""]
        ]

        # Exibe o menu formatado com tabulate
        print(tabulate(opcoes, headers=["=====", "Menu", "===="], tablefmt="grid"))

        # Solicita a escolha do usuário
        opcao = input("Escolha uma opção: ").strip()

        # Executa a ação correspondente à opção escolhida
        if opcao == "1":
            cadastrar_curriculo()
        elif opcao == "2":
            listar_curriculos()
        elif opcao == "3":
            buscar_curriculo()
        elif opcao == "4":
            atualizar_curriculo()
        elif opcao == "5":
            excluir_curriculo()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa chamando a função menu
menu()