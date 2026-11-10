class Solution:
    def sum_of_digits(n):
        sum = 0
        while(n > 0):
            b = n%10
            n = n//10
            sum += b * b
        return sum

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            print(Solution.sum_of_digits(n))
            n = Solution.sum_of_digits(n)
            if(n == 1):
                return True
        return False