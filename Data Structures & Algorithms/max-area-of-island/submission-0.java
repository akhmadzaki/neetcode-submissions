class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        Set<List<Integer>> visitedCell = new HashSet<>(); 
       int maxArea = 0;
       int currentArea = 0;
       int[][] bounds = {
        {0,1}, {0,-1}, {-1,0}, {1,0}
       };

       for(int i = 0; i < grid.length; ++i) {
            for(int j = 0; j < grid[0].length; ++j) {
                if(grid[i][j] == 0 || visitedCell.contains(Arrays.asList(i,j))) continue;
                else {
                    currentArea = 0;
                    Deque<List<Integer>> d = new LinkedList<>();
                    d.push(Arrays.asList(i,j));
                    while(!d.isEmpty()) {
                        List<Integer> currentCell = d.pop();
                        if(!visitedCell.contains(currentCell)) {
                            visitedCell.add(currentCell);
                            currentArea++;
                            for(int[] bound: bounds) {
                                int dx = currentCell.get(0) + bound[0];
                                int dy = currentCell.get(1) + bound[1];

                                if(dx >= 0 && dx < grid.length && dy >= 0 && dy < grid[0].length && grid[dx][dy] == 1)
                                {
                                    d.push(Arrays.asList(dx, dy));
                                }
                            }
                        }
                    }
                    maxArea = Math.max(maxArea, currentArea);
                }
            }
       }

       return maxArea;
    }
}
