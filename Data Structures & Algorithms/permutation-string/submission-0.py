class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Hashmap = {}
        s2Hashmap = {}

        for i in range(len(s1)):
            if s1[i] not in s1Hashmap:
                s1Hashmap[s1[i]] = 1
            else:
                s1Hashmap[s1[i]] += 1

        for r in range(len(s2)):
            char = s2[r]
            s2Hashmap[char] = s2Hashmap.get(char, 0) + 1

            if r >= len(s1):
                leftChar = s2[r - len(s1)]
                if s2Hashmap[leftChar] == 1:
                    del s2Hashmap[leftChar]
                else:
                    s2Hashmap[leftChar] -= 1

            if s1Hashmap == s2Hashmap:
                return True
        
        return False