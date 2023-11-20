def count_rooms(mapa):
    n = len(mapa)
    m = len(mapa[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        if visited[i][j]:
            return
        visited[i][j] = True
        if mapa[i][j] == '#':
            return
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and mapa[i][j] == '.':
                count += 1
                dfs(i, j)

    return count

# Ejemplo de uso:
mapa = [
    "########",
    "#..#...#",
    "####.#.#",
    "#..#...#",
    "########"
]

result = count_rooms(mapa)
print(result)  