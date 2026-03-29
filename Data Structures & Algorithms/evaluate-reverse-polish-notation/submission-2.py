class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        # 22
        arr = ["+", "-", "*", "/"]
        res = 0
        stack = []
        for token in tokens:
            if token not in arr:
                stack.append(token)
            elif token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(str(int(second) + int(first)))
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(str(int(second) - int(first)))
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(str(int(second) * int(first)))
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(str(int(int(second) / int(first))))

        return int(stack[0])
        
                