def encontrar_camino(mapa):
    n = len(mapa)
    m = len(mapa[0])
    visitados = [[False for _ in range(m)] for _ in range(n)]
    direcciones = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    inicio, fin = None, None
    for i in range(n):
        for j in range(m):
            if mapa[i][j] == 'A':
                inicio = (i, j)
            elif mapa[i][j] == 'B':
                fin = (i, j)

    cola = [(inicio, 0, "")]  # (coordenadas, longitud del camino, descripción del camino)

    while cola:
        actual, longitud, camino = cola.pop(0)
        i, j = actual

        if actual == fin:
            return 'SÍ', longitud, camino

        if i < 0 or i >= n or j < 0 or j >= m:
            continue
        if visitados[i][j] or mapa[i][j] == '#':
            continue

        visitados[i][j] = True

        for direccion, movimiento in direcciones.items():
            ni, nj = i + movimiento[0], j + movimiento[1]
            cola.append(((ni, nj), longitud + 1, camino + direccion))

    return 'NO'

# Ejemplo de uso:
mapa = [
    "########",
    "#.A#...#",
    "#.##.#B#",
    "#......#",
    "########"
]

resultado = encontrar_camino(mapa)
print(resultado)  