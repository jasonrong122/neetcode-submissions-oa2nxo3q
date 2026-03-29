class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { 
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in hashmap:
                if stack[-1] == hashmap[c]:
                    stack.pop()
            else:
                stack.push(c)
        
        return stack.empty()