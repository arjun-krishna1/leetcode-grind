# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
GIVEN
INPUT
head of a singly linked list
reverse the list
return the reversed list

e.g.
1 -> 2 -> 3 -> 4 -> 5 : 1 <- 2 <- 3 <- 4 <- 5

1 -> 2 : 1 <- 2

BRUTE FORCE O(N) time (iterate through the entire linked list, non-nested) O(N) space (store values in linked list)
iterate through list and get list of values
reverse list of values
construct linked list from list
return new linked list

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        vals = []
        
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        vals.reverse()
        
        new_head = ListNode(val=vals[0])
        curr = new_head
        
        for i in range(1, len(vals)):
            node = ListNode(val=vals[i])
            curr.next = node
            curr = curr.next
            
        return new_head
        
OPTIMIZATIONS
- instead of copying all values, why not just switch the position of the nodes in the linked list?
algorithm:
    prev = head, curr = head.next
    prev.next = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return curr
    
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head or not head.next:
                return head

            prev = head
            curr = head.next
            prev.next = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev


    

'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(curr):
            # base case: if only one node, it is reversed
            if not curr.next:
                return curr

            # recursive case
            else:
                # recursively reverse the rest of the linked list
                new_head = helper(curr.next)
                # the tail of the reversed linked list should now point to curr
                curr.next.next = curr
                # current is now the tail and should point to None
                curr.next = None
                # return the head of the reversed linked list
                return new_head
                
        # edge case, if 0 or 1 node, already reversed
        if not head or not head.next:
                return head
                
        # recursively reverse list
        return helper(head)
        
