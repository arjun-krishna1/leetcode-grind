'''
https://leetcode.com/problems/longest-common-subsequence/
https://leetcode.com/submissions/detail/547317748/
# Self-critique:
## Positive:
- I'm very happy that I came up with a working, efficient algorithm for this complex problem!!!! 🚀 🎉
- this is a classic dynamic programming problem
- we want longest common substring of two long strings (complex problem)
- so first we get the longest common substring of each part of each string (smaller, simpler subproblems)
- we add one char to the algorithm at a time and build it to the answer of the big complex problem
## Negative:
- I didn't solve it as fast as I could have
  - I should have first walked through the algorithm in detail
  - Specifically how we choose what to use as the longest common substring when there are multiple options
  - And how to add a character to the previous lcs when we have matching characters
- My solution wasn't optimal
# How to improve next time?
- Write down specific algorithm for problem before jumping into code
  - a finite sequence of well-defined instructions
  - Nothing should be left up to the imagination
- Practice more dynamic programming problems

Whooo! Super proud of myself for solving this

# Optimal Solution
- After watching the conceptual walkthrough of this problem
- I used that to crate a consistently faster than 85% solution
- The video thought about it recursively, with the elements above, to the left and on the diagonal
- represting solutions to the recursive subproblems
- And using that information instead of some other complex logic
'''
def removeAllDistinct(str1, str2):
	i = 0
	while i < len(str1):
		# this char will never be in the common subsequence
		if str1[i] not in str2:
			# remove it and all other occurences of it
			chr_remove = str1[i]
			str1 = str1.replace(chr_remove, "")
		
		else:
			i += 1
			
	j = 0
	while j < len(str2): # O(N**2)
		if str2[j] not in str1:
				chr_remove = str2[j]
				str2 = str2.replace(chr_remove, "")
		
		else:
			j += 1
				
	return str1, str2

class Solution(object):
    def longestCommonSubsequence(self, str1, str2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # remove all chars in str1 that are not in str2 and vice versa
        str1, str2 = removeAllDistinct(str1, str2)
        #print(str1, str2)
        # start the last row of table as empty strings
        last_row = ["" for i in range(len(str1) + 1)]

        # iterate through all the chars in str2
        # at each char add it to the substring of str2 we are using to build
        # the longest common subsequence
        for i in range(1, len(str2) + 1):
            # hold the longest common subsequence of this substring of str2 and
            # at each char of str1 in new_row
            new_row = [""]
            # iterate through each char in str1
            for j in range(1, len(str1) + 1):
                # if the chars in str1 and str2 are the same
                if str1[j - 1] == str2[i - 1]:
                    # get the lcs without the last two characters
                    # in each string and add this common character
                    # to the end of that lcs
                    new_row.append(last_row[j - 1] + str1[j - 1])

                else:
                    # get the longest lcs of str1 without the
                    # last considered character and str2 without the same
                    # and set that as this lcs
                    if len(new_row[-1]) >= len(last_row[j]):
                        new_row.append(new_row[-1])

                    else:
                        new_row.append(last_row[j])

            # update last_row to be new_row
            last_row = new_row

        # return the lcs of all of str1 and str2, split into a list of chars		
        return len(last_row[-1])
        
"""
# dynamic programming tabulation, original
def removeAllDistinct(str1, str2):
	i = 0
	while i < len(str1):
		# this char will never be in the common subsequence
		if str1[i] not in str2:
			# remove it and all other occurences of it
			chr_remove = str1[i]
			str1 = str1.replace(chr_remove, "")
		
		else:
			i += 1
			
	j = 0
	while j < len(str2): # O(N*M)
		if str2[j] not in str1:
				chr_remove = str2[j]
				str2 = str2.replace(chr_remove, "")
		
		else:
			j += 1
				
	return str1, str2
	
def longestCommonSubsequence(str1, str2):
	# remove all chars in str1 that are not in str2 and vice versa
	str1, str2 = removeAllDistinct(str1, str2)
	print(str1, str2)
	# start the last row of table as empty strings
	last_row = ["" for i in range(len(str1) + 1)]
	
	table = [last_row]
	# iterate through all the chars in str2
	# at each char add it to the substring of str2 we are using to build
	# the longest common subsequence
	for i in range(1, len(str2) + 1): # O(N^2*M)
		# hold the longest common subsequence of this substring of str2 and
		# at each char of str1 in new_row
		new_row = [""]
		# iterate through each char in str1
		for j in range(1, len(str1) + 1):
			# start the lcs of this place in the table as the last lcs
			new_elem = new_row[-1]
			
			# if the chars in str1 and str2 are the same
			if str1[j - 1] == str2[i - 1]:
				max_count = min(str1.count(str1[j - 1]), str2.count(str2[i - 1])) # how can we remove these counts? they are destroying the time complexity
				curr_count = new_elem.count(str1[j - 1])
				
				if curr_count < max_count:
					# add it to this new lcs
					new_elem += str1[j - 1]
			
			# if the lcs in the last row was longer than this one
			if len(last_row[j]) > len(new_elem):
				# abandon this new lcs and use the one in the last row
				new_elem = last_row[j]
					
			# add this element to new_row
			new_row.append(new_elem)
			
		# update last_row to be new_row
		last_row = new_row
		table.append(last_row)
	print(table)
		
	# return the lcs of all of str1 and str2, split into a list of chars		
	return list(last_row[-1])
	
# dynamic programming with memoization:
from collections import defaultdict

def longestCommonSubsequence(str1, str2):
	hashmap = defaultdict(lambda: -1)
	def helper(str1, str2):
		# base case, one is an empty string
		if not str1 or not str2:
			return ""

		# answer is cached
		elif hashmap[(str1, str2)] != -1:
			return hashmap[(str1, str2)]
			
		# recursive case:
		else:
			# if the last characters are the same
			if str1[-1] == str2[-1]:
				# get the lcs of the start of the str
				# without common char
				# add common char to the end of the str
				
				if hashmap[(str1[:-1], str2[:-1])] == -1:
					hashmap[(str1[:-1], str2[:-1])] = helper(str1[:-1], str2[:-1])
					
				hashmap[(str1, str2)] = hashmap[(str1[:-1], str2[:-1])] + str1[-1]
				return hashmap[(str1, str2)]
			else:
				# get the lcs of the strings by ignoring the 
				# ending at a time
				
				if hashmap[(str1, str2[:-1])] == -1:
					hashmap[(str1, str2[:-1])] = helper(str1, str2[:-1])
				if hashmap[(str1[:-1], str2)] == -1:
					hashmap[(str1[:-1], str2)] = helper(str1[:-1], str2)
				str1_ans = hashmap[(str1, str2[:-1])]
				str2_ans = hashmap[(str1[:-1], str2)]

				if len(str2_ans) > len(str1_ans):
					str1_ans = str2_ans

				return str1_ans
	return list(helper(str1, str2))
			

"""
