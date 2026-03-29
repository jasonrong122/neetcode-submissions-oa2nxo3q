class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}
        
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        my_list = []
        for k, v in my_dict.items():
            if v >= k:
                my_list.append(k)
        
        return my_list