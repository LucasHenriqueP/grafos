import json
from classes.vertice import Vertice
from classes.aresta import Aresta

with open('exemplos.json') as f:
    y = json.loads(f.read())

print(y["vertice"][0])

#Todo o codigo abaixo deve ir para a classe Grafo

vertices = list() # talvez vire um vetor
arestas = list()
for i in range(len(y['vertice'])):
    v0 = Vertice(y["vertice"][i])
    vertices.append(v0)

for i in range(len(y['aresta'])):
    a0 = Aresta(y['aresta'][i])
    arestas.append(a0)



for v in vertices:
    for a in arestas:
        if(a.origem == v.nome):
            v.addAresta(a)
        if(a.destino == v.nome):
            v.addGrauEntrada    


print(len(vertices[0].aresta))

