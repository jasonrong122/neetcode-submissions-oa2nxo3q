class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, num)
                    nextPerms.append(pCopy)
            perms = nextPerms
            
        res = set()
        for p in perms:
            res.add(tuple(p))
            
        return list(res)