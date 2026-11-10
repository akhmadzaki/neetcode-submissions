class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_area = 0

        def isValid(y,x):
            return (x >= 0 and x < cols) and (y >= 0 and y < rows)

        def dfs(r,c):
            current_area = 1
            stack = []
            stack.append((r,c))
            visited[r][c] = True

            x_coord = [1, -1, 0, 0]
            y_coord = [0, 0, 1, -1]

            while len(stack) > 0:
                (y,x) = stack.pop()

                #check: not visited, in grid bound, and an island
                for i in range(4):
                    neighbor_x = x + x_coord[i]
                    neighbor_y = y + y_coord[i]
                    # print(neighbor_y, neighbor_x)
                    if isValid(neighbor_y, neighbor_x) and grid[neighbor_y][neighbor_x] == 1 and (not visited[neighbor_y][neighbor_x]):
                        visited[neighbor_y][neighbor_x] = True
                        stack.append((neighbor_y, neighbor_x))
                        current_area += 1
            return current_area

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1 and (not visited[r][c])):
                    current_area = dfs(r,c)
                    max_area = max(max_area, current_area)
                
        return max_area