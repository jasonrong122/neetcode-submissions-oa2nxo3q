class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for x in operations:
            if x == "D":
                stack.append(2 * stack[-1])
            elif x == "C":
                stack.pop()
            elif x == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(x))
        
        res = 0
        for num in stack:
            res += num
        
        return res