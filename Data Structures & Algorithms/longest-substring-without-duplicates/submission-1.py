class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 1
        windowSet = set()
        windowSet.add(s[l])
        res = 1

        while r < len(s):
            if s[r] not in windowSet:
                windowSet.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                windowSet.remove(s[l])
                l += 1

        return res