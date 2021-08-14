"""
https://leetcode.com/problems/read-n-characters-given-read4/
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file

ALGORITHM


"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        def build_str(l):
            res = ""
            for i in l:
                if i != 0:
                    res += i
            return res
        
        buf4 = [0 for i in range(4)]
        last_addition = read4(buf4)
        curr_loc = 0
        chars_added = 0
        
        while last_addition > 0 and n - curr_loc > 0:
            chars_to_add = min(last_addition, n - curr_loc)
            chars_added += chars_to_add
            for i in range(chars_to_add):
                buf[curr_loc + i] = buf4[i]
            curr_loc += last_addition
            last_addition = read4(buf4)
        return chars_added
        
