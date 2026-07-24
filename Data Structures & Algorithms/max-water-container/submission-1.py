class Solution:
    def maxArea(self, height: List[int]) -> int:
        # l = 0
        # res = 0

        # for r in range(1, len(height)):
        #     res = max(res, (r - l) * min(height[l], height[r]))
        #     if height[r] > height[l]:
        #         l = r

        # return res

        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return res