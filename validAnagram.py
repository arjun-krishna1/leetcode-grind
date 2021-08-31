'''
GIVEN
INPUT
    two strings s and t
    
OUTPUT
    return True if t is an anagram of s, and Fals otherwise
    
    anagram -> same characters, can be in differen torders
    
    BRUTE FORCE O(n*m) time, O(1) space
        iterate through each character in s: idx i
            find first occurence of s[i] in t at j
                pop i and j
            if no occurence
                return False
                
    OPTIMIZATIONS
    HASHMAP O(n) time, O(1) space (max length of 26 as only 26 chars in english)
        instead of having to go through each string twice
        if length is different return False
        iterate through s 
            increase count of this char by 1
            
        iterate through t
            if count is 0
                return False
            reduce this count by 1
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = defaultdict(lambda: 0)
        
        for i in s:
            count[i] += 1
            
        for i in t:
            if count[i] <= 0:
                return False
            
            count[i] -= 1
            
        return True
            
    SORTING O(n*log(n)) time, O(1) space
        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            s = list(s)
            t = list(t)
            s.sort()
            t.sort()
            return s == t
        
            
'''
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = defaultdict(lambda: 0)
        
        for i in s:
            count[i] += 1
            
        for i in t:
            if count[i] <= 0:
                return False
            
            count[i] -= 1
            
        return True
        
