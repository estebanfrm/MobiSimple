import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(grafo, origen=None, destino=None):
    G = nx.Graph()

    # Agrega nodos
    for nodo in grafo:
        G.add_node(nodo)

    # Agrega aristas
    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            G.add_edge(nodo, vecino, weight=peso)

    # Posiciones fijas para una visualización clara
    pos = nx.spring_layout(G, seed=42)

    # Definir colores
    colores = []
    for nodo in G.nodes():
        if nodo == origen:
            colores.append("green")
        elif nodo == destino:
            colores.append("red")
        else:
            colores.append("skyblue")

    # Dibujar nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color=colores, node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

    plt.title("Mapa de rutas")
    plt.show()
