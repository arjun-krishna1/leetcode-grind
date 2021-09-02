'''
GIVEN
INPUT
nums: integer array

OUTPUT
return all triplets [nums[i], nums[j], nums[k]] where i, j and k are unique
and nums[i] + nums[j] + nums[k] == 0

BRUTE FORCE O(n**3) time, O(1) space
three nested for loops
    if indexes are all different and they sum to zero
        add to list
        
HASHING
- how to handle duplicate triplets?
- how to make sure that there are triplets where each number is unique? set?
create a hashmap
two nested loops
    if not equal
        add their sum to hashmap as key and value is the two numbers

iterate through nums: i
    if negative of this number is in hashmap
        add triplet to result
        
HOW TO OPTIMIZE?
solution must not contain duplicate triplets
-> remove duplicates from

output should only have unique outputs, even if there are multiple duplicates
-> can we just remove dupicates from input?
    no... because sometimes duplicates are needed
'''
from collections import defaultdict
class Solution(object):
    def threeSum(self, array):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Initialize set to hold results:
        results = set()
        #Sort the input:
        array.sort()

        #Loop through each object in the array and fix the first_pointer
        for first_pointer in range(len(array)-2):
            #Initialize two pointers based on the first, fixed pointer:
            second_pointer = first_pointer + 1
            third_pointer = len(array) - 1

            #loop while second_pointer is before third_pointer:
            while second_pointer < third_pointer:
                #Calculate the sum of the three pointed elements
                this_sum = array[first_pointer] + array[second_pointer] + array[third_pointer]

                # if this is a result
                if this_sum == 0:
                    results.add((array[first_pointer], array[second_pointer], array[third_pointer]))
                    second_pointer += 1

                #Move second_pointer forward if this sum is less than the target
                if this_sum < 0 :
                    second_pointer += 1

                #Move the third_pointer backward if this sum is more than the target
                elif this_sum > 0:
                    third_pointer -= 1

        # we are returning a set, is this okay?
        return results
