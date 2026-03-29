class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        stack = []

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                stack.append(temperatures[j])
                count = 0
                if stack[-1] > temperatures[i]:
                    while stack:
                        stack.pop()
                        count += 1
                    arr.append(count)
                    count = 0
                    break
                elif j == len(temperatures) - 1:
                    arr.append(0)
                    break

        return arr