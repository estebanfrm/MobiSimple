#Definimos las aristas del grafo
edges = [
    [0, 1, 5],
    [0, 2, 3],
    [1, 2, 2],
    [1, 3, 6],
    [2, 3, 7],
    [2, 4, 4],
    [3, 4, 2],
    [3, 5, 8],
    [4, 5, 1]
]

#Construimos el grafo como diccionario de listas de adyacencia
def construir_grafo():
    graph = {}

    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
    
        graph[u].append((v, w))
        graph[v].append((u, w))  # como es bidireccional

    return graph