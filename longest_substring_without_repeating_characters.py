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
        
