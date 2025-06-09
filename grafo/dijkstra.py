import heapq

def dijkstra_simple(grafo, origen):
    #Diccionario de distancias mínimas desde el nodo origen
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0

    #Diccionario de predecesores para reconstruir la ruta
    predecesores = {nodo: None for nodo in grafo}

    #Cola de prioridad para explorar nodos más cercanos primero
    heap = [(0, origen)]

    while heap:
        distancia_actual, nodo_actual = heapq.heappop(heap)

        if distancia_actual > distancias[nodo_actual]:
            continue  #Nodo ya procesado con mejor distancia

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))

    return distancias, predecesores

def reconstruir_ruta(predecesores, destino):
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = predecesores[actual]
    ruta.reverse()
    return ruta
