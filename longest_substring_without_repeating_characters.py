'''
GIVEN
INPUT
s: string

OUTPUT
length of the longest substring without repeating characters

ALGORITHM
BRUTE FORCE
two nested for loops generate every possible substring
    if substring doesn't have repeating chars update max_count if needed
    
OPTIMIZATIONS
SLIDING WINDOW
instead of considering every possible substring
just have two pointers, left and right which define a substring
create a hashmap to hold the chars in the current substring
keep moving right to the right until there is a repeated character
update maxlen if needed
move left to the right and reduce its count

OPTIMIZE
create a mapping of the chars to its index, skip the chars immediately when we find a repeated char

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize pointers and result
        l, res = 0, 0
        
        # char_map
        char_map = {}
        
        # keep moving and making window larger while it is within the string
        for r in range(len(s)):
            # if this is a repeating character
            if s[r] in char_map:
                # skip to one past the last seen location of this character
                l = max(char_map[s[r]], l)
           
            res = max(res, r - l + 1)
            char_map[s[r]] = r + 1
        return res
                
        
        
