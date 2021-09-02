class Solution(object):
    '''
    GIVEN
    INPUT
    strs: array of strings
    
    OUTPUT
    group the anagrams together
    anagram: word or phrase formed by rearranging the letters of a different word or phrase
             using all the original letters exactly once
             
    BRUTE FORCE
    iterate through each word in strs
        count how many of each characters is in the string
        find al lother words with same number of characters and add to result
        skip already consideres trings
    output result
    
    SET -> won't work, we need to know number of each char as well, not just total length and unique chars
    create a defaultdict with empty list as default
    iterate through each word
        turn this word to a set
        add this word to the list at key this set
        
    SORT
    turn list into tuple with sorted word and initial word
    sort the list
    iterate through the list and add the second element in the tuple to this result list
    
     def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        for i in range(len(strs)):# O(n*m*log(m))
            strs[i] = (sorted(strs[i]), strs[i]) # O(m*log(m)) -> sorting time
            
        
        
        res = []
        i = 0
        while i < len(strs): # O(n) time
            this_res = []
            j = i
            # add all the words that are anagrams to this result
            while j < len(strs) and strs[i][0] == strs[j][0]:
                this_res.append(strs[j][1])
                j += 1
            # add this group of anagrams to total result
            res.append(this_res)
            # skip to end of anagrams
            i = j
        return res
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cache = defaultdict(lambda: [])
        for i in range(len(strs)):
            cache[tuple(sorted(strs[i]))].append(strs[i])
            
        res = []
        for i in cache:
            res.append(cache[i])
        
        return res
            
    ''' 
    from collections import defaultdict
            
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def countChars(word):
            res = [0 for i in range(26)]
            for i in word:
                res[ord(i) - ord("a")] += 1

            return tuple(res)
        
        cache = defaultdict(lambda: [])
        for i in range(len(strs)):
            cache[countChars(strs[i])].append(strs[i])
            
        res = []
        for i in cache:
            res.append(cache[i])
        
        return res
        
