class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ls = []
        for i in operations:
            if(i == '+'):
                ls.append(int(ls[-1]) + int(ls[-2]))
            elif(i == 'D'):
                ls.append(2 * int(ls[-1]))
            elif(i == 'C'):
                ls.pop()
            else:
                ls.append(int(i))
        return sum(ls)