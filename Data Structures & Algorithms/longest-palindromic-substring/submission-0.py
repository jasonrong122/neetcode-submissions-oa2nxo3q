class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = ""

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                length = max(length, r - l + 1)
                if r - l + 1 >= length:
                    res = s[l:r + 1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                length = max(length, r - l + 1)
                if r - l + 1 >= length:
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res