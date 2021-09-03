class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_max(m):
            if not len(m):
                return 0
            return max(chars_map.values())
            
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        # start and end of the window
        # and the max length of the window
        start = 0
        end = 0
        curr_max_len = 0
        
        # keep track of the count of characters
        # and the number of unique chars
        chars_map = {}
        
        # while the end of the window is within the string
        # keep moving the window forward
        while end < len(s):
            # while this window has less than k chars to replace
            # so all chars except the most common char in this window
            # keep making the window bigger by moving end forward
            while end < len(s) and end - start - get_max(chars_map) <= k:
                # if this is a new character
                if s[end] not in chars_map:
                    # create a count for it
                    chars_map[s[end]] = 1
                
                # this character has been seen before, update this characters count
                else:
                    chars_map[s[end]] += 1
                    
                # move end forward
                end += 1
            
            # take this windows size
            curr_max_len = max(curr_max_len, end - start - 1)
            
            if end - start - get_max(chars_map) <= k:
                curr_max_len = max(curr_max_len, end - start)
            
            # make the window smaller by moving the start pointer forward
            # until we get a valid number of characters again
            while end < len(s) and end - start - get_max(chars_map) > k:
                # move start pointer forward one forward one
                start += 1

                # update the counter of the character we left
                chars_map[s[start - 1]] -= 1
                # if this character has no more characters in the window
                if chars_map[s[start - 1]] == 0:
                    # remove this key
                    del chars_map[s[start - 1]]
        return curr_max_len
        
