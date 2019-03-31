class Vertice:
    def __init__(self, nome):
        self.valor = 0
        self.nome = nome
        self.aresta = list()
        self.__grauEntrada = 0
        self.__grauSaida = 0

    def addAresta(self, aresta):
        self.aresta.append(aresta)
        self.__grauSaida +=1

    def getGrauEntrada(self):
        return self.__grauEntrada
        
    def getGrauSaida(self):
        return self.__grauSaida
        
