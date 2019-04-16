class Vertice:
    def __init__(self, args):
        #self.valor = args['valor']
        self.nome = args
        self.aresta = list()
        self.__grauEntrada = 0
        self.__grauSaida = 0

    def addAresta(self, a):
        print("TO NA CLASSE VERTICE", a)
        self.aresta.append(a)
        self.__grauSaida +=1

    def getGrauEntrada(self):
        return self.__grauEntrada

    def getGrauSaida(self):
        return self.__grauSaida

    def addGrauEntrada(self):
        self.__grauEntrada += 1

    def __repr__(self):
        return str("Vertice %s" %(self.nome) )    
        pass