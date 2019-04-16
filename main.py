
from classes.grafo import Grafo

from classes.vertice import Vertice

vertices = list()


with open('exemplo.txt', 'r') as f:
    linha = f.readline()
    while(linha != '0 0'):
        print(linha)
        linha = linha.replace('\n', '')
        print(type(linha))
        lista = list()
        lista = linha.split(' ')
        if(len(lista) == 1):
            k = int(lista[0]) -1
            ver = list()
            for i in range(1,int(lista[0])+1):
                v = Vertice(i)
                ver.append(v)
            for i in range(k-1):
                linha = f.readline()
                #print(line)
                lista_vertice = list()
                lista_vertice = linha.split(' ')
                for v in ver:
                    print(int(lista_vertice[0]))

                    if int(lista_vertice[0]) == int(v.nome):
                        #print("ENTRRRROU")
                        v.addAresta(lista_vertice[1])
                        #print('Arresta', v.aresta[0])

                    if int(lista_vertice[1]) == int(v.nome):
                        #print("ENTRRRROU")
                        v.addAresta(lista_vertice[0])
                        #print('Arresta', v.aresta[0])
                           

            vertices.append(ver)            


for vert in vertices:
    for v in vert:
        print(v)
        for a in v.aresta:
            print(a)



grafo = Grafo('exemplos.json')


