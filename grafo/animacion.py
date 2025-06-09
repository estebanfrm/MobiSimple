from tqdm import tqdm
import time
#Se instala tqdm desde la terminal

def animar_ruta(grafo, ruta):
    print("\n🧭 Iniciando viaje...\n")
    for i in range(len(ruta) - 1):
        origen = ruta[i]
        destino = ruta[i+1]

        # Buscar el peso entre origen y destino
        peso = next(w for v, w in grafo[origen] if v == destino)

        print(f"→ De {origen} a {destino} ({peso} seg)")
        for _ in tqdm(range(peso), desc=f"Viajando {origen}→{destino}", unit="s"):
            time.sleep(1)
