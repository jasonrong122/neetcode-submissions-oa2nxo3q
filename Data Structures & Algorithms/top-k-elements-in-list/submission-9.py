class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}
        
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        
        my_list = []
        for i in range(k):
            my_list.append(my_dict.keys[i])
        
        return my_list[0]