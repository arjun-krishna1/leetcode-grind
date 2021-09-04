'''
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
GIVEN
INPUT
string s

OUTPUT
length of longest substring without repeating characters

BRUTE FORCE
four nested for loops
    the first loop is the start of the subset
    the second loop is the end of the subset
    the third and fourth loops compare each element with the substring with each other element
        breaks out of the three inner loops and moves the start to the next point
    keep the largest difference between start and end and return it
        
OPTIMIZATIONS
two moving pointers
    -> then we can remove the first two loops
    -> start = 0, end = 1
        -> increase end until there is a repeating character
        -> then move start to one past the first repeating character, keep end where it is
        -> keep going
        -> keep the largest difference to start and end, then remove it
hash-map checkup
- use a hashmap with 26 keys
    - each key is a letter of the alphabet
    - the value is either -1 or an integer
    - if -1 the character hasn't happened yet
    - else the integer is the index of the last place where the character is
- when checking the current substring
- see if the new character's value in the hashmap is not -1
    - if so this is not a valid substring
    - move start to one past the value in the hashmap
    
OPTIMIZED ALGORITHM
start = 0
end = 0

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        # create a hashmap to hold the last location of each char in the current substring
        hashmap = {}
        for i in s:
            hashmap[i] = -1

        missing_val = -1
        max_len = 0

        # initialize two pointers
        # start is the first char in this substring
        start = 0
        # end is one past the end of the substring
        end = 0

        while end < len(s):
            end += 1

            # last char in substring is repeated
            if hashmap[s[end - 1]] != -1 and hashmap[s[end - 1]] >= start:
                # may have to go through all values before this one and make them -1 again?
                start = max(hashmap[s[end - 1]] + 1, start + 1)

            hashmap[s[end - 1]] = end - 1

            # new max_len
            if end - start > max_len:
                max_len = end - start

        return max_len
'''
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

dp approach

'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case: if less than 1 characters, no repeating chars
        # return all of s
        if len(s) <= 1:
            return len(s)
        
        # initialize pointers and result
        l, r, res = 0, 0, 0
        # initialize hashmap to hold number of each char
        count = defaultdict(lambda: 0)
        
        # keep moving and making window larger while it is within the string
        while r < len(s):
            # add this new character to the count
            count[s[r]] += 1
            # if it is a repeating character
            # this is an invalid substring
            while count[s[r]] > 1:
                # make the window smaller by
                # moving the left pointer right and updating its count
                # print(l)
                count[s[l]] -= 1
                l += 1
            
            # since this character is not repeating
            # this is a valid substring
            else:
                res = max(r - l + 1, res)
                r += 1
            # print(l, r)
            # print(dict(count))
        return res
        
