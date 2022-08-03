import class_lista_principal

def bem_vindo():
    print("O que deseja fazer?")
    print("1 - Adicionar um Gênero")
    print("2 - Adicionar um Jogo")
    print("3 - Visualizar generos existentes")
    print("4 - Visualizar jogos dentro de um genero existente")
    print("5 - Remover um Gênero")
    print("6 - Remover um jogo")

def verificar_numero():
    escolha = input("Número: ")
    try:
        escolha = int(escolha)
        if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6:
            print("O número digitado é inválido, favor tentar novamente!")
            return verificar_numero()
        else:
            return escolha
    except:print("Dados inválidos")

def adicionar_genero():
    genero = input("Digite o gênero: ")
    if len(genero) == 0:
        print("Conteudo está em branco\n")
    elif len(genero) >0 and len(genero) <3:
        print("Favor inserir um gênero com pelo menos 3 caracteres")
    else:
        menu.adicionar_genero(genero)

def remover_genero():
    print("Remover um gênero irá também remover todos os jogos dentro dele, deseja continuar?")
    sim_ou_nao = input("S/N: ")
    if sim_ou_nao == "S" or sim_ou_nao == "s":
        print_generos()
        print("Qual gênero gostaria de remover? ")
        escolha = input("Genero: ")
        menu.remover_genero(escolha)
    else: print("Usuário escolheu não continuar\n voltando para o menu principal!\n")

def remover_jogo():
    print("Qual gênero o jogo pertence?")
    menu.print_genero()
    genero_rem_jogo = input("Gênero o jogo: ")
    menu.print_jogos(genero_rem_jogo)
    print("Qual o jogo que será removido?")
    jogo_rem = input("Jogo a ser removido: ")
    menu.remover_jogo(genero_rem_jogo,jogo_rem)

def adicionar_jogo():
    jogo_inserido = 0
    while jogo_inserido == 0:
        jogo = input("Digite o nome do jogo: ")
        if len(jogo) == 0:print("Conteudo está em branco\n")
        elif len(jogo) > 0 and len(jogo) < 3:print("Favor inserir um jogo com pelo menos 3 caracteres")
        else:
            while jogo_inserido == 0:
                preco = input("Digite o preco do jogo: ")
                if len(preco) == 0:print("Conteudo está em branco\n")
                else:
                    preco = float(preco.replace(',', '.'))
                    while jogo_inserido == 0:
                        genero = input("Digite a qual genero o jogo pertence: ")
                        if len(genero) == 0:print("Conteudo está em branco\n")
                        elif len(genero) > 0 and len(jogo) < 3:print("Favor inserir um genero com pelo menos 3 caracteres")
                        else:
                            menu.adicionar_jogo(jogo,preco,genero)
                            jogo_inserido = 1

def print_generos():
    print("-" * 90)
    menu.print_genero()
    print("-" * 90)

def print_jogos_genero():
    genero_print = input("Qual gênero gostaria de visualizar os jogos?: ")
    print("-" * 90)
    menu.print_jogos(genero_print)
    print("-" * 90)

menu = class_lista_principal.Steam()
print("Bem vindo a Steam criada por Ícaro Aurich")
while True:
    bem_vindo()
    escolha = verificar_numero()
    if escolha == 1: # 1 - Adicionar um Gênero
        adicionar_genero()
    elif escolha == 2: # 2 - Adicionar um Jogo
        adicionar_jogo()
    elif escolha == 3: # 3 - Visualizar generos existentes
        print_generos()
    elif escolha == 4: # 4 - Visualizar jogos dentro de um genero existente
        print_jogos_genero()
    elif escolha == 5: # 5 - Remover um gênero
        remover_genero()
    elif escolha == 6: # remover jogo
        remover_jogo()