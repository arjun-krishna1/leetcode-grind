class Solution(object):
    """
    GIVEN
    INPUT
        nums: an array of integers
        target: integer
        
    OUTPUT
        indices of the two numbers such that they add up to targe
            note, want indices not value
        
    ASSUME
        exactly one solution
        may not use the same element twice
        can return the answer in any order
        
    BRUTE FORCE O(N**2) time, iterate through the list in nested fashion
        iterate through list once
            iterate through array again
                skip if same index
                return if add up to target
                
    OPTIMIZATION this is also O(N*log(n)) time, O(1) space
        sort?
        use property that if a + b = target -> target - a = b
        sort the array 
        iterate a through list
            calculate b
            binary search forward from this index, and find b
            
        hashmap O(N) time, O(N) space, two pass hash table
        cache: create a default dictionary that returns -1 if number is not in array
        
        iterate through nums
            make value of cache[num] the index
            duplicates will get overwritten, doesn't matter, there is exactly one solution
                what if it is half -> check half edge case
            
        iterate through nums
            get b
            check if b is in cache
                return this index and index of b 
    """
    from collections import defaultdict
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = defaultdict(lambda: -1)
        
        # build cache
        for i in range(len(nums)):
            # edge case where half of target is in nums twice
            if cache[nums[i]] != -1 and 2*nums[i] == target:
                return [cache[nums[i]], i]
            
            cache[nums[i]] = i
            
        # search for result
        for i in range(len(nums)):
            b = target - nums[i]
            # edge case where cache[b] == i, don't return that
            if cache[b] != -1 and cache[b] != i:
                return [i, cache[b]]
        
