class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res