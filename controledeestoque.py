print("Bem-vindo(a) ao Controle de Estoque da Bicicletaria da Franciele da Cruz Sousa!")

# Lista para armazenar as peças cadastradas
listaPecas = []

# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    dicionarioPeca = {} #dicionário para armazenar os dados da peça

    print("Você selecionou a Opção de Cadastrar Peça")
    print("Código da peça: {}".format(codigo))

    # Pede os dados da peça para o usuário
    nome = input("Por favor entre com o NOME da peça: ")
    fabricante = input("Por favor entre com o FABRICANTE da peça: ")
    valor = float(input("Por favor entre com o VALOR (R$) da peça: "))

    # Preenche o dicionário com os dados da peça
    dicionarioPeca["codigo"] = codigo
    dicionarioPeca["nome"] = nome
    dicionarioPeca["fabricante"] = fabricante
    dicionarioPeca["valor"] = f'{valor:.2f}'

    # Adiciona o dicionário à lista de peças
    listaPecas.append(dicionarioPeca.copy())

# Função para consultar peças
def consultarPeca():
    while True:
        try:
            print("Você selecionou a Opção de Consultar Peças")
            consultar = int(input("Entre com a opção desejada: \n"
                                  "1-Consultar Todas as Peças \n"
                                  "2-Consultar Peças por Código \n"
                                  "3-Consultar Peças por Fabricante \n"
                                  "4-Retornar\n>>"))

            if consultar == 1:
                print("-"*20)

                for peca in listaPecas:
                    for key, value in peca.items():
                        print("{} : {}".format(key, value))
                    print("-"*20)

            elif consultar == 2:
                print("-"*20)
                entrada = int(input("Digite o código desejado: "))
                for peca in listaPecas:
                    if peca["codigo"] == entrada:
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
                        print("-"*20)

            elif consultar == 3:
                print("-"*20)
                entrada = input("Digite o fabricante da peça: ")
                for peca in listaPecas:
                    if peca["fabricante"] == entrada:
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
                        print("-"*20)

            elif consultar == 4:
                break

            else:
                print("Digite uma opção válida")
                continue

        except ValueError:
            print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")

# Função para remover uma peça
def removerPeca():
    print("Você selecionu remover Peça")
    entrada = int(input("Digite o código da peça a ser removida: "))
    for peca in listaPecas:
        if peca["codigo"] == entrada:
            listaPecas.remove(peca)
            print("Peça removida.")

# Variável para controlar o código da peça
codigo = 0

while True:
    try:
        # Solicita a opção desejada ao usuário
        opcao = int(input("Escolha a opção desejada: \n"
                          "1-Cadastrar Peças \n"
                          "2-Consultar Peças \n"
                          "3-Remover Peças \n"
                          "4-Sair\n>>"))

        if opcao == 1:
            # Incrementa o código da peça e chama a função de cadastrar peça
            codigo += 1
            cadastrarPeca(codigo)

        elif opcao == 2:
            consultarPeca()

        elif opcao == 3:
            removerPeca()

        elif opcao == 4:
            print("Programa finalizado")
            break

        else:
            print("Digite uma opção válida")
            continue

    except ValueError:
        print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")