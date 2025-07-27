# You are given a 2D grid of '1's (land) and '0's (water).
# An island is formed by connecting adjacent lands horizontally or vertically.
# Return the number of islands in the grid.

from collections import deque

def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'  # mark as visited

        while queue:
            row, col = queue.popleft()
            directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'  # mark visited

    # main loop through grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                island_count += 1

    return island_count