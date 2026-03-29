class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = 0

        for i in range(len(s)):
            hashset = set()
            hashset.add(s[i])
            count = 1
            res = max(res, count)
            for j in range(i + 1, len(s)):
                if s[j] not in hashset:
                    hashset.add(s[j])
                    count += 1
                    res = max(res, count)
                else:
                    break

        return res