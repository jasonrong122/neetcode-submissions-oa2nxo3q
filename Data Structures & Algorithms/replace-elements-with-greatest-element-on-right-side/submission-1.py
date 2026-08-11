class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        for i in range(len(arr) - 1):
            curr = 0
            for j in range(i + 1, len(arr)):
                curr = max(curr, arr[j])
            res[i] = curr

        return res