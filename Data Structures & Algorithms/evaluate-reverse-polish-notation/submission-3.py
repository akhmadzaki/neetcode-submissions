class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in tokens:
            if i == "+":
                result = int(stack.pop()) + int(stack.pop())
                stack.append(str(result))
            elif i == "-":
                right = stack.pop()
                left = stack.pop()
                result = int(left) - int(right)
                stack.append(str(result))
            elif i == "*":
                result = int(stack.pop()) * int(stack.pop())
                stack.append(str(result))
            elif i == "/":
                right = stack.pop()
                left = stack.pop()
                result = int(int(left) / int(right))
                stack.append(str(result))
            else: 
                stack.append(i)
        return int(stack[-1])
            
        