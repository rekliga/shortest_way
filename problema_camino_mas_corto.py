from collections import deque


def camino_mas_corto(grid, start, end):
    n = len(grid)

    if not (
        0 <= start[0] < n and 0 <= start[1] < n and 0 <= end[0] < n and 0 <= end[1] < n
    ):
        print("El punto de inicio o fin está fuera de la matriz")
        return -1

    if grid[start[0]][start[1]] != 0 or grid[end[0]][end[1]] != 0:
        print("Obstacle")
        return -1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start[0], start[1], 1)])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, dist = queue.popleft()
        print(f"Visitando nodo: ({x}, {y}), distancia: {dist}")
        if (x, y) == (end[0], end[1]):
            return dist - 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and grid[nx][ny] == 0
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    print("No se encontró un camino al destino.")
    return -1


# Ejemplo de uso
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
]
print(camino_mas_corto(grid, (0, 0), (3, 3)))  # Salida esperada: 6
