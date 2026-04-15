class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [""]
        numberToLetter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" :"wxyz"
        }
        res = []
        combSet = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(combSet))
                return
            
            key = digits[i]
            for c in numberToLetter[key]:
                combSet.append(c)
                dfs(i + 1)
                combSet.pop()

        dfs(0)
        return res