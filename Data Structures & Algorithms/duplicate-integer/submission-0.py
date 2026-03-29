class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        count += 1
        if count > 0:
            return True
        else:
            return False