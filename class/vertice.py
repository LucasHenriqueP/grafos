class Vertice:
    def __init__(self, nome):
        self.valor
        self.nome = nome
        self.aresta = list()
        self.grauEntrada = 0
        self.grauSaida = 0

    def addAresta(self, aresta):
        self.aresta.append(aresta)
        
