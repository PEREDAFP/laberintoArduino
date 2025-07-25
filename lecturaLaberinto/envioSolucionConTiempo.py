import sys
import json
import time
from collections import deque

DIRECCIONES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
NOMBRES_DIRECCIONES = ['derecha', 'abajo', 'izquierda', 'arriba']

def cargar_laberinto(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return [list(linea.rstrip('\n')) for linea in archivo]

def encontrar_punto(laberinto, objetivo):
    for fila, linea in enumerate(laberinto):
        for columna, valor in enumerate(linea):
            if valor == objetivo:
                return fila, columna
    return None

def bfs(laberinto, inicio, fin):
    cola = deque()
    cola.append((inicio, []))
    visitados = set()
    visitados.add(inicio)

    while cola:
        (fila, col), camino = cola.popleft()

        if (fila, col) == fin:
            return camino + [(fila, col)]

        for dy, dx in DIRECCIONES:
            nueva_fila, nueva_col = fila + dy, col + dx
            if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_col < len(laberinto[0]):
                if laberinto[nueva_fila][nueva_col] != 'X' and (nueva_fila, nueva_col) not in visitados:
                    visitados.add((nueva_fila, nueva_col))
                    cola.append(((nueva_fila, nueva_col), camino + [(fila, col)]))

    return []

def direccion_de_a(p1, p2):
    dy, dx = p2[0] - p1[0], p2[1] - p1[1]
    return DIRECCIONES.index((dy, dx))

def camino_a_acciones(camino):
    acciones = []
    if not camino or len(camino) < 2:
        return acciones

    direccion_actual = direccion_de_a(camino[0], camino[1])
    pasos = 1

    for i in range(1, len(camino) - 1):
        nueva_direccion = direccion_de_a(camino[i], camino[i + 1])

        if nueva_direccion == direccion_actual:
            pasos += 1
        else:
            if pasos > 0:
                acciones.append({"accion": "avanza", "espacio": pasos})
                pasos = 1

            if (direccion_actual + 1) % 4 == nueva_direccion:
                acciones.append({"accion": "derecha", "espacio": 0})
            elif (direccion_actual - 1) % 4 == nueva_direccion:
                acciones.append({"accion": "izquierda", "espacio": 0})
            else:
                acciones.append({"accion": "derecha", "espacio": 0})
                acciones.append({"accion": "derecha", "espacio": 0})

            direccion_actual = nueva_direccion

    if pasos > 0:
        acciones.append({"accion": "avanza", "espacio": pasos})

    return acciones
   
def imprimir_laberinto_con_camino(laberinto, camino):
    laberinto_con_camino = [fila[:] for fila in laberinto]  # copia profunda
    camino_set = set(camino)  # para búsqueda rápida

    print("\nSolución del laberinto:\n")
    for fila_idx, fila in enumerate(laberinto_con_camino):
        linea_impresa = ''
        for col_idx, char in enumerate(fila):
            if (fila_idx, col_idx) in camino_set and char == ' ':
                linea_impresa += '\033[92mI\033[0m'  # I en verde
            else:
                linea_impresa += char
        print(linea_impresa)
    print()
    
def enviar_acciones(acciones, retardo):
    print("Instrucciones JSON:\n")
    for accion in acciones:
        json_str = json.dumps(accion)
        # Aquí imprimiría en consola, pero podrías usar serial.write(json_str.encode()) si usas pyserial
        print(json_str)
        time.sleep(retardo)


def main():
    if len(sys.argv) < 2:
        print("Uso: python laberinto.py <archivo_laberinto> [retardo_segundos]")
        return

    archivo_laberinto = sys.argv[1]
    retardo = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5  # valor por defecto: 0.5 segundos

    laberinto = cargar_laberinto(archivo_laberinto)
    inicio = encontrar_punto(laberinto, 'E')
    fin = encontrar_punto(laberinto, 'S')

    if not inicio or not fin:
        print("No se encontró 'E' o 'S' en el laberinto.")
        return

    camino = bfs(laberinto, inicio, fin)
    if not camino:
        print("No se encontró un camino de 'E' a 'S'.")
        return

    acciones = camino_a_acciones(camino)
    imprimir_laberinto_con_camino(laberinto, camino)
    enviar_acciones(acciones, retardo)

if __name__ == "__main__":
    main()
