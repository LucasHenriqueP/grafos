import json

vertice =  '[{ "name":"v1", "valor":30}, {"name": "v2", "valor":40}]'
aresta = '{"digrafo": 0}[{"nome":"a0", "v0": "v1", "v1": "v2"}]'

# parse x:
y = json.loads(vertice)
x = json.loads(aresta)


# the result is a JSON string:
print(y[1]["name"])
print(x[0]['v0'])