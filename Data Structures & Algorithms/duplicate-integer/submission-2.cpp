class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() == 0)
        {
            return false;
        }

        for (int i = 0; i < nums.size() - 1; i++)
        {
            for (int j = 1; j <= nums.size() - 1; j++)
            {
                if (i != j)
                {
                    if (nums[i] == nums[j])
                    {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
};
