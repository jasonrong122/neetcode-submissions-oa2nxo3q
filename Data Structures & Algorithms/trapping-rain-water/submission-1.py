class Solution:
    def trap(self, height: List[int]) -> int:
        trappedRain = 0
        temp = 0

        l = 0
        for r in range(1, len(height)):
            if height[l] > height[r]:
                temp += height[l] - height[r]
            else:
                l = r
                trappedRain += temp
                temp = 0

        temp = 0
        r = len(height) - 1
        for l in range(len(height) - 2, -1, -1):
            if height[r] >= height[l]:
                temp += height[r] - height[l]
            else:
                r = l
                trappedRain += temp
                temp = 0
            
        return trappedRain