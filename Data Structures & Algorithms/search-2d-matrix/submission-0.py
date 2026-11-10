class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1

        mid = (left + right)//2

        while left <= right:
            #convert mid to x,y
            #3,4 -> 4 = 1,0  num//cols, num%cols
            r = mid//cols
            c = mid%cols

            if matrix[r][c] == target:
                return True

            if matrix[r][c] < target:
                left = mid+1
            else:
                right = mid-1
            mid = (left + right)//2
        return False
            
        