# Agenda é uma lista que irá armazenar nomes e telefones
agenda = []

# Variável para marcar se houve alguma alteração na agenda
alterada = False

def pede_nome(padrão=""):
    """
    Função que solicita o nome ao usuário.
    Se o usuário não digitar nada, retorna o valor padrão.
    """
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome

def pede_telefone(padrão=""):
    """
    Função que solicita o telefone ao usuário.
    Se o usuário não digitar nada, retorna o valor padrão.
    """
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

def mostra_dados(nome, telefone):
    """
    Função que exibe o nome e o telefone.
    """
    print(f"Nome: {nome} Telefone: {telefone}")

def pede_nome_arquivo():
    """
    Função que solicita o nome do arquivo ao usuário para salvar ou carregar a agenda.
    """
    return input("Nome do arquivo: ")

def pesquisa(nome):
    """
    Função que pesquisa um nome na agenda.
    Retorna o índice do nome na lista se encontrado, caso contrário, retorna None.
    """
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    """
    Função para adicionar um novo contato na agenda.
    Se o nome já existir, exibe uma mensagem de erro.
    """
    global agenda, alterada
    nome = pede_nome()
    if pesquisa(nome) is not None:  # Verifica se o nome já existe
        print("Erro: Nome já existe na agenda.")
        return
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    alterada = True

def confirma(operação):
    """
    Função que solicita confirmação ao usuário para uma operação.
    Retorna True se o usuário confirmar, False caso contrário.
    """
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção == "S"
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    """
    Função para apagar um contato da agenda.
    """
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento"):
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

def altera():
    """
    Função para alterar um contato existente na agenda.
    Permite alterar o nome e/ou telefone.
    """
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        novo_nome = pede_nome(nome)  # Permite alterar o nome
        if novo_nome != nome and pesquisa(novo_nome) is not None:
            print("Erro: Nome já existe na agenda.")
            return
        telefone = pede_telefone(telefone)  # Permite alterar o telefone
        agenda[p] = [novo_nome, telefone]
        alterada = True
    else:
        print("Nome não encontrado.")

def listar():
    """
    Função para listar todos os contatos da agenda.
    """
    print("\nAgenda")
    print("-" * 60)
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("-" * 60)

def executa():
    """
    Função principal que controla a execução do programa.
    """
    while True:
        print("\n1 - Novo")
        print("2 - Alterar")
        print("3 - Apagar")
        print("4 - Listar")
        print("0 - Sair")
        opção = input("Escolha uma opção: ")
        if opção == "0":
            if alterada:
                if confirma("gravação antes de sair"):
                    nome_arquivo = pede_nome_arquivo()
                    grava(nome_arquivo)
            print("Saindo...")
            break
        elif opção == "1":
            novo()
        elif opção == "2":
            altera()
        elif opção == "3":
            apaga()
        elif opção == "4":
            listar()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executa()


