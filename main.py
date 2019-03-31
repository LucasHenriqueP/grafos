import json
from classes.vertice import Vertice 

with open('exemplos.json') as f:
    y = json.loads(f.read())

print(len(y["aresta"]))

v0 = Vertice("nome")
print(v0.getGrauSaida())
v0.addAresta(5)
print(v0.getGrauSaida())