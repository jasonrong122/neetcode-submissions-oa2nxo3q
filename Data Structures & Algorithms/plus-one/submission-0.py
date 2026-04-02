class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""

        for i in digits:
            res += str(i)

        result = int(res) + 1

        arr = []
        for i in str(result):
            arr.append(int(i))

        return arr