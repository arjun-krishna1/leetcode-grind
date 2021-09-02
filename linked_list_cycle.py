# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
GIVEN
INPUT
    head of linked list
    
OUTPUT
    boolean, does the linked list have a cycle in it
        cycle, some node in the list that can be reached again by continuously
        following the next pointer
        return true if there is a cycle in the linked list
        otherwise false
        
BRUTE FORCE O(N**2) time O(N) space
    build a list of nodes
    iteate through linked list starting at head
        at each new nead check if it is already in the list
OPTIMIZATION hash table O(N) time O(N) space
    iterate throug linked list
        if this node is already in the hashtable there is a cycle
        add this node to hashtable
    no cycle
    """
        :type head: ListNode
        :rtype: bool
        """
        # edge case: if list is empty or has an ending, no cycle
        if not head or not head.next:
            return False
        
        curr = head
        hashmap = {}
        while curr.next:
            # is already in hashmap, there is a cycle
            if curr in hashmap:
                return True
            # mark as visited
            hashmap[curr] = True
            # move to next node
            curr = curr.next
        # there was no cycle
        return False
        
OPTIMIZATION two pointer
think about two pointers, fast and slow
fast moves twice, slow moves once
if fast gets to end, we know there is no cycle, if end no cycle
if there is a cycle, if you repeat this enough times fast and slow will be the same eventually 

class Solution(object):
     def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # edge case: if list is empty or has an ending, no cycle
        if not head or not head.next:
            return False
        
        # two pointers, one fast, one slow
        fast = head.next.next
        slow = head.next
 
        # while we are not at the end of the list and fast and slow are different
        while fast and fast.next and fast != slow:
            # move fast forward twice as fast as slow
            fast = fast.next.next
            slow = slow.next
        
        # if they were the same there was a cycle
        if fast == slow:
            return True
        
        # else there is no cycle
        return False
        
'''
class Solution(object):
     def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # edge case: if list is empty or has an ending, no cycle
        if not head or not head.next:
            return False
        
        history = set()
        curr = head
 
        # while we are not at the end of the list and this node is not visited
        while curr and curr not in history:
            # mark this node as visited
            history.add(curr)
            curr = curr.next
        
        # if this was visited there is a ycle
        if curr and curr in history:
            return True
        
        # else there is no cycle
        return False
        
