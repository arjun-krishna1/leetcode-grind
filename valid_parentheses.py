'''
GIVEN
INPUT
    s: string containing '(', ')', '{', '}', '[' and ']'
    
OUTPUT
    determine if string is valid
        open brackets are closed by the same type of brackets
        open brackets must be closed in the correct order
        
BRUTE FORCE O(N) time, O(1) space -> won't work, will miss some edge cases where brackets are wrong order
    iterate through string
        count how many opening brackets of each type
        decrease if closing bracket
        if negative return False
        
    if any are positive return False
    
    return True
STACK
    create empty stack
    iterate through string
        if opening push onto stack
        if closing pop from stack
            if not matching, return False
    return True

    this is a very good use of a stack,
'''
opening = ['(', '{', '[']
closing = {')': '(', '}': '{', ']': '['}
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i in opening:
                stack.append(i)
                
            else:
                if not len(stack):
                    return False
                
                top = stack.pop()
                #print(top, i, closing[i])
                # if closing does not match opening return False
                if top != closing[i]:
                    return False
                
        return len(stack) == 0
        
