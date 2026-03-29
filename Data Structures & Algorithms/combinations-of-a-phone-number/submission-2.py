class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [""]
        
        numberToLetter = {'2' : ["a", "b", "c"],
                          '3' : ["d", "e", "f"],
                          '4' : ["g", "h", "i"],
                          '5' : ["j", "k", "l"],
                          '6' : ["m", "n", "o"],
                          '7' : ["p", "q", "r", "s"],
                          '8' : ["t", "u", "v"],
                          '9' : ["w", "x", "y", "z"]}

        res = []

        def dfs(i, currSet):
            if len(currSet) == len(digits):
                res.append("".join(currSet))
                return

            currentDigit = digits[i]
            for letter in numberToLetter[currentDigit]:
                currSet.append(letter)
                dfs(i + 1, currSet)
                currSet.pop()

        
        dfs(0, [])
        return res