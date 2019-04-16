import json

from classes.vertice import Vertice
from classes.aresta import Aresta

class Grafo:
    def __init__(self, exemploJason):

        with open(exemploJason) as f:
            y = json.loads(f.read())

        print(y["vertice"][0])
        #Todo o codigo abaixo deve ir para a classe Grafo
        self.vertices = list() # talvez vire um vetor
        self.arestas = list()
        '''
        for i in range(len(y['vertice'])):
            v0 = Vertice(y["vertice"][i])
            print(v0)
            self.vertices.append(v0)


        for i in range(len(y['aresta'])):
            a0 = Aresta(y['aresta'][i])
            self.arestas.append(a0)

        for v in self.vertices:
            for a in self.arestas:
                if(a.origem == v.nome):
                    v.addAresta(a)
                if(a.destino == v.nome):
                    v.addGrauEntrada


        print(len(self.vertices[0].aresta))
        '''