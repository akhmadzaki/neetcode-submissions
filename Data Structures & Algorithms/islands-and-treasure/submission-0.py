class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #multi-source BFS
        #for each treasure, we BFS to all land cells connected to it

        rows = len(grid)
        cols = len(grid[0])

        def isValid(r,c):
            return (r >= 0 and r < rows) and (c >= 0 and c < cols)

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        r_offset = [-1, 1, 0, 0]
        c_offset = [0, 0, -1, 1]

        while queue:
            r,c = queue.popleft()

            for i in range(4):
                nr = r + r_offset[i]
                nc = c + c_offset[i]

                if isValid(nr, nc) and grid[nr][nc] > 0:
                    if grid[nr][nc] > (grid[r][c] + 1):
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))
        
        