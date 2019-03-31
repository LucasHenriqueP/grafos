class Aresta:
    def __init__(self, args):
        self.nome = args['name']
        self.valor = args['valor']
        self.origem = args['v0']
        self.destino = args['v1']


    def __repr__(self):
        return str("De %s para %s" % (self.origem, self.destino))

