import class_lista_secundaria

class Menu():
    def __init__(self,genero_jogo):
        self.genero = genero_jogo
        self.list_jogos = None
        self.prox_gen = None

class Steam:
    def __init__(self,):
        self.catalogo = None

    def remover_genero(self,genero):
        existe = self.existe_genero(genero)
        if existe == 0:
            print("Genero",genero,"não existe!\n")
        else:
            removido = 0
            aux = self.catalogo
            while removido == 0:
                if aux.genero == genero: #remover o primeiro
                    self.catalogo = self.catalogo.prox_gen
                    removido = 1
                elif aux.prox_gen.genero == genero:
                    aux.prox_gen = aux.prox_gen.prox_gen
                    removido = 1
                else:
                    aux = aux.prox_gen
            print("Genero",genero,"foi removido")

    def remover_jogo(self,genero_jogo,nome_jogo):
        existe = self.existe_genero(genero_jogo)
        if existe == 0:
            print(genero_jogo, "Não existe")
        else:
            existe_nome_jogo = self.existe_jogo(nome_jogo,genero_jogo)
            if existe_nome_jogo == 0:
                print("Jogo",nome_jogo,"não existe no catalogo")
            else:
                aux = self.catalogo
                removido = 0
                aux2 = aux.list_jogos
                while removido == 0:
                    if str(aux.genero) == str(genero_jogo):
                        while removido == 0:
                            if aux.list_jogos.jogo == nome_jogo:  # remover o primeiro
                                aux.list_jogos = aux.list_jogos.prox_jogo
                                removido = 1
                            else:
                                while removido == 0:
                                    if aux2.prox_jogo.jogo == nome_jogo:
                                        aux2.prox_jogo = aux2.prox_jogo.prox_jogo
                                        removido = 1
                                    else:
                                        aux2 = aux2.prox_jogo
                        print("Jogo", nome_jogo, "foi removido")
                        removido = 1
                    else:
                        aux = aux.prox_gen
                return existe

    def adicionar_genero(self,genero_jogo):
        existe = self.existe_genero(genero_jogo)
        if existe == 1:
            print("genero",genero_jogo,"já existente\n")
        else:
            if self.catalogo == None:
                self.catalogo = Menu(genero_jogo)
                print("Genero", genero_jogo, "adicionado com sucesso!\n")
            else:
                aux = self.catalogo
                novo_jogo = Menu(genero_jogo)
                if str(aux.genero) > str(genero_jogo):
                    novo_jogo.prox_gen = self.catalogo
                    self.catalogo = novo_jogo
                else:
                    while True:
                        if aux.prox_gen == None:
                            aux.prox_gen = Menu(genero_jogo)
                            print("Genero",genero_jogo,"adicionado com sucesso!\n")
                            break
                        elif str(aux.prox_gen.genero) > str(genero_jogo):
                            novo_jogo.prox_gen = aux.prox_gen
                            aux.prox_gen = novo_jogo
                            break
                        else:
                            aux = aux.prox_gen

    def print_genero(self):
        aux = self.catalogo
        var = "||"
        while aux is not None:
            var = var + str(aux.genero) + " || "
            aux = aux.prox_gen
        print(var)

    def existe_genero(self,genero_jogo):
        aux = self.catalogo
        existe = 0
        while aux is not None:
            if str(aux.genero) == str(genero_jogo):
                existe = 1
                break
            else:
                aux = aux.prox_gen
        return existe

    def existe_jogo(self,nome_jogo,genero_jogo):
        aux = self.catalogo
        existe = 0
        fim = 0
        while aux is not None and fim == 0:
            if aux.list_jogos == None:
                return existe
            else:
                if str(aux.genero) == str(genero_jogo):
                    aux = aux.list_jogos
                    while aux is not None:
                        if str(aux.jogo) == str(nome_jogo):
                            existe = 1
                            fim = 1
                            break
                        else:
                            aux = aux.prox_jogo
                else:
                    aux = aux.prox_gen
        return existe

    def adicionar_jogo(self,nome_jogo,preco_jogo,genero_jogo):
        def sucesso():
            print("Jogo",nome_jogo,"adicionado com sucesso!\n")
        existe = self.existe_genero(genero_jogo)
        if existe == 0: print(genero_jogo, "Não existe")
        else:
            existe_nome_jogo = self.existe_jogo(nome_jogo,genero_jogo)
            if existe_nome_jogo == 1:
                print("Jogo",nome_jogo,"já existe no catalogo")
            else:
                aux = self.catalogo
                aux2 = self.catalogo
                jogo = class_lista_secundaria.Lista_Secundaria(nome_jogo,preco_jogo)
                while aux is not None:
                    if str(aux.genero) == str(genero_jogo):
                        aux2 = aux.list_jogos
                        while aux is not None:
                            if aux2 == None:
                                aux.list_jogos = jogo
                                sucesso()
                                break
                            elif str(jogo.jogo) < str(aux2.jogo):
                                jogo.prox_jogo = aux2
                                aux2.ant_jogo = jogo
                                aux.list_jogos = jogo
                                sucesso()
                                break
                            elif aux2.prox_jogo == None:
                                aux2.prox_jogo = jogo
                                jogo.ant_jogo = aux2
                                break
                            elif str(jogo.jogo) < str(aux2.prox_jogo.jogo):
                                jogo.prox_jogo = aux2.prox_jogo
                                aux2.ant_jogo = jogo
                                aux2.prox_jogo = jogo
                                break
                            else:
                                aux2 = aux2.prox_jogo
                        break
                    else:
                        aux = aux.prox_gen

    def print_jogos(self,genero_jogo):
        aux = self.catalogo
        while aux is not None:
            if aux.genero == genero_jogo:
                aux = aux.list_jogos
                var = "Jogos do genero: " + genero_jogo
                print(var)
                var = ""
                while aux is not None:
                    print(aux.jogo,": R$", aux.preco)
                    # var = var + str(aux.list_jogos.jogo) + " = R$: "
                    # var = var + str(aux.list_jogos.preco) + " || "
                    aux = aux.prox_jogo
                print(var)
            else:
                aux = aux.prox_gen