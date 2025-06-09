from auth.register import register_user
from auth.login import login_user

FILE_PATH = "data/users.txt"

def main():
    print("1. Registrarse")
    print("2. Iniciar sesión")
    choice = input("Elige una opción: ")

    if choice == "1":
        register_user(FILE_PATH)
    elif choice == "2":
        login_user(FILE_PATH)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    
    main()

# LLAMAR LA FUNCION DEL GRAFO
from grafo.grafo import construir_grafo

grafo = construir_grafo()


#LLAMAR A LA FUNCION GRAFO VISUAL

from grafo.grafo_visual import visualizar_grafo

# Mostrar el grafo
visualizar_grafo(grafo)

# Pedir origen y destino
origen = int(input("Ingrese el nodo de origen (0-5): "))
destino = int(input("Ingrese el nodo de destino (0-5): "))

# Mostrar grafo resaltando origen y destino
visualizar_grafo(grafo, origen, destino)

#Importar dijktra & la animacion

from grafo.dijkstra import dijkstra_simple, reconstruir_ruta
from grafo.animacion import animar_ruta

# Calcular camino más corto
distancias, predecesores = dijkstra_simple(grafo, origen)
ruta = reconstruir_ruta(predecesores, destino)

# Mostrar resultado
print(f"\nRuta más corta: {' → '.join(map(str, ruta))}")
print(f"Costo total: {distancias[destino]}")

# Animación
animar_ruta(grafo, ruta)

#Costo & limpieza
TARIFA_POR_SEGUNDO = 2000 
# Calcular tiempo total de la ruta
tiempo_total = distancias[destino]
costo_total = tiempo_total * TARIFA_POR_SEGUNDO

print(f"\n🕒 Tiempo total: {tiempo_total} segundos")
print(f"💰 Costo del viaje: ${costo_total:.2f}")

print("\n🔁 Reiniciando sistema para el siguiente pasajero...\n")
