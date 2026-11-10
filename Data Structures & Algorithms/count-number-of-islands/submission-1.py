class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs 
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0

        def isValid(y,x):
            return (x >= 0 and x < cols) and (y >= 0 and y < rows)

        def dfs(r,c):
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
                    if isValid(neighbor_y, neighbor_x) and grid[neighbor_y][neighbor_x] == '1' and (not visited[neighbor_y][neighbor_x]):
                        visited[neighbor_y][neighbor_x] = True
                        stack.append((neighbor_y, neighbor_x))

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1' and (not visited[r][c])):
                    dfs(r,c)
                    count += 1
        return count


    

                
    




        