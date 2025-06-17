import random

def generar_laberinto(ancho, alto):
    # Crear laberinto lleno de muros
    laberinto = [['X'] * ancho for _ in range(alto)]

    # Función para elegir posición aleatoria en borde
    def pos_borde():
        lado = random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
        if lado == 'arriba':
            return (0, random.randint(1, ancho - 2))
        elif lado == 'abajo':
            return (alto - 1, random.randint(1, ancho - 2))
        elif lado == 'izquierda':
            return (random.randint(1, alto - 2), 0)
        else:
            return (random.randint(1, alto - 2), ancho - 1)

    # Elegir entrada y salida en bordes distintos
    entrada = pos_borde()
    salida = pos_borde()
    while salida == entrada:
        salida = pos_borde()

    # Poner entrada y salida
    laberinto[entrada[0]][entrada[1]] = 'E'
    laberinto[salida[0]][salida[1]] = 'S'

    # Rellenar el interior con espacios o muros aleatorios
    for i in range(1, alto -1):
        for j in range(1, ancho -1):
            laberinto[i][j] = ' ' if random.random() > 0.3 else 'X'

    # Asegurar espacios libres junto a entrada y salida para accesibilidad
    for r, c in [entrada, salida]:
        if r == 0:
            laberinto[r+1][c] = ' '
        elif r == alto -1:
            laberinto[r-1][c] = ' '
        if c == 0:
            laberinto[r][c+1] = ' '
        elif c == ancho -1:
            laberinto[r][c-1] = ' '

    return laberinto

def guardar_laberinto(laberinto, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        for fila in laberinto:
            f.write(' '.join(fila) + '\n')

def main():
    print("Generador aleatorio de laberintos")
    ancho = int(input("Introduce ancho (mínimo 5): "))
    alto = int(input("Introduce alto (mínimo 5): "))
    if ancho < 5 or alto < 5:
        print("Ancho y alto deben ser al menos 5 para que tenga sentido.")
        return

    laberinto = generar_laberinto(ancho, alto)
    nombre_archivo = "laberinto_generado.txt"
    guardar_laberinto(laberinto, nombre_archivo)
    print(f"Laberinto generado y guardado en '{nombre_archivo}'")

if __name__ == "__main__":
    main()
