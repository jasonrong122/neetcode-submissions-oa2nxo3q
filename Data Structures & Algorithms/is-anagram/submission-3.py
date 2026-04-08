class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHashmap = {}
        tHashmap = {}

        for i in range(len(s)):
            if s[i] not in sHashmap:
                sHashmap[s[i]] = 1
            else:
                sHashmap[s[i]] += 1

            if t[i] not in tHashmap:
                tHashmap[t[i]] = 1
            else:
                tHashmap[t[i]] += 1

        return sHashmap == tHashmap