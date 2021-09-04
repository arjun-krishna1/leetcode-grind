'''
# looked at solution and copied code from there. need to revisit this later.
## What did I miss?
- jumped into code too soon
- first come up with algorithm, optimize it
- then jump into code
- once you start coding it becomes hard to switch back into algorithm design
- instead of rechecking each time, the map was updated one at a time

GIVEN
INPUT
s, t: two strings of lengths m and n

OUTPUT
return the minimum window substring of s
such that every character in t (including duplicates) is included in the window
"" if no such substring
assume such answer us unique

a substring is a contiguous sequence of characters within the string

THOUGHTS
the smallest substring in s
that has all the characters in t
including the same numbers

sliding window?

ALGORITHM
BRUTE FORCE
start = 0
size = len(t)
end = size
while size < len(s):
    for start in range(len(s) - size):
        if included(s[start:start + size], t):
            return s[start:start + size]
    size += 1
return ""

def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(lambda: 0)
        for i in t:
            t_map[i] += 1
        
        def includes(substr):
            char_map = defaultdict(lambda: 0)
            # count characters in substr
            for i in substr:
                char_map[i] += 1
                
            # make sure that each character in t is included in char_map
            for i in t_map:
                if char_map[i] < t_map[i]:
                    return False
            return True
        
        # if even the entire string is not enough, there is no such window substring
        if not includes(s):
            return ""
        
        elif s == t:
            return s
        
        elif len(s) < len(t):
            return ""

        # increase the window size
        for size in range(len(t), len(s)):
            for start in range(len(s) - size + 1):
                if includes(s[start: start + size]):
                    return s[start: start + size]
EXAMPLE
ADOBECODEBANC, ABC

ADO -> doesn't have B, C make window bigger

OPTIMIZATION
instead of checking each window
make each window start on a character in t
    start end at start + len(k)
    if it has enough characters make this the result
    else keep moving end forward until it has all the required characters
    if this reaches the end, return last min

    def minWindow(self, s: str, t: str) -> str:
        # count the characters in t
        t_map = defaultdict(lambda: 0)
        for i in t:
            t_map[i] += 1 
            
        # if even the entire string is not enough, there is no such window substring
        if not includes(s):
            return ""
        
        elif s == t:
            return s
        
        elif len(s) < len(t):
            return ""
            
        # start the window at each location in s
        max_str = s
        j = len(t)
        for i in range(len(s)):
            # keep increasing the size of the window while
            # it is a valid window
            while j < len(s) + 1:
                # if this is a desirable substring
                if includes(s[i:j]):
                    # if this is a new minimum desirable substring
                    if len(s[i:j]) < len(max_str):
                        max_str = s[i:j]
                j += 1
        return max_str
'''
from collections import Counter
class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        
        required = len(dict_t)
        
        l, r = 0, 0
        
        formed = 0
        
        window_counts = {}
        
        ans = float("inf"), None, None
        
        while r < len(s):
            
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                window_counts[char] -= 1

                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
                
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
