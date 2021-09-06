class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        # get the frequency of each number
        for i in nums: # O(n)
            if i in count:
                count[i] += 1
                
            else:
                count[i] = 1
        
        count_vals = []
        
        # turn it into tuples of the form (freq, num)
        for i in count: # O(n)
            count_vals.append((count[i], i))
        
        
        # sort in descending order so higher frequency is first
        count_vals.sort(reverse = True) # O(n*log(n))
        
        res = []
        
        # add the k most frequent to result
        for i in range(k):
            res.append(count_vals[i][1])
        
        # return the k most frequent numbers
        return res
        
