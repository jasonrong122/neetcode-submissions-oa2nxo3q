class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}" : "{",
                   ")" : "(",
                   "]" : "["}

        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0 or hashmap[c] != stack[-1]:
                    return False
                else:
                    stack.pop()

        if not stack:
            return True

        return False