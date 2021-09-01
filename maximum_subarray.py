class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        curr_max = -float('inf')
        global_max = -float('inf')
        
        for i in nums:
            # if this number is larger than this number plus current max
            # make current max just this number
            curr_max = max(i, curr_max + i)
                
            # if current max is a new global max
            global_max = max(curr_max, global_max)
                
        return global_max
        
