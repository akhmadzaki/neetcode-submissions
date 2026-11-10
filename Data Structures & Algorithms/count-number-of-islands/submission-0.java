class Solution {
    public int numIslands(char[][] grid) {
       Set<List<Integer>> visitedCell = new HashSet<>(); 
       int islandCount = 0;
       int rows = grid.length;
       int cols = grid[0].length;

       for(int i = 0; i < grid.length; ++i) {
            for(int j = 0; j < grid[0].length; ++j) {
                if(grid[i][j] == '0' || visitedCell.contains(Arrays.asList(i,j))) continue;
                else {
                    Deque<List<Integer>> d = new LinkedList<>();
                    System.out.print(i);System.out.print(j);System.out.print(" ");
                    d.push(Arrays.asList(i,j));
                    while(!d.isEmpty()) {
                        List<Integer> currentCell = d.pop();
                        if(!visitedCell.contains(currentCell)) {
                            visitedCell.add(currentCell);
                            List<List<Integer>> neighbors = getNeighbors(grid, currentCell.get(0), currentCell.get(1));
                            for(List<Integer> n: neighbors) {
                                System.out.print(n.get(0));System.out.print(n.get(1));System.out.print(" ");
                                d.push(n);
                            }
                        }
                    }
                    System.out.println();
                    islandCount++;
                }
            }
       }

       return islandCount;
    }

    public List<List<Integer>> getNeighbors(char[][] grid, int i, int j) {
        List<List<Integer>> ret = new ArrayList<>();
        int rows = grid.length;
        int cols = grid[0].length;

        if(grid[i][j] == '1') {
            if(i > 0) ret.add(Arrays.asList(i-1,j));
            if(i < rows - 1) ret.add(Arrays.asList(i+1,j));
            if(j > 0) ret.add(Arrays.asList(i,j-1));
            if(j < cols -1) ret.add(Arrays.asList(i,j+1));
        }
        
        return ret;
    }
}
