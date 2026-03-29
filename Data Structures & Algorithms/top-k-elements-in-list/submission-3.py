class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}
        
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        my_list = []
        for key, value in my_dict.items():
            if value >= k:
                my_list.append(key)
        
        return my_list