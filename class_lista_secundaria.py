class Lista_Secundaria:
    def __init__(self,nome_jogo,preco_jogo):
        self.jogo = nome_jogo
        self.preco = preco_jogo
        self.ant_jogo = None
        self.prox_jogo = None