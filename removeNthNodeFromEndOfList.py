# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
GIVEN
INPUT
head of linked list

OUTPUT
remove the nth node from the end of the list and return its head

ALGORITHM
have curr as head
prev_remove is also head
dist_prev_curr is 0

move curr forward while it is not null:
    curr = curr.next
    dist_prev_curr += 1
    if dist_prev_curr > n + 1:
        prev_remove = prev_remove.next
        dist_prev_curr -= 1
temp = prev_remove.next.next
prev_remove.next = None
prev_remove.next = temp
return head
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        curr = head
        # we want this to be n + 1'th node from the end
        prev_remove = head
        dist = 0
        
        while curr.next:
            curr = curr.next
            dist += 1
            # if we're too far behind
            if dist > n:
                prev_remove = prev_remove.next
                dist -= 1
        
        if dist < n:
            temp = head.next
            head = None
            return temp
        
        
        # remove the nth node if it is not None
        if prev_remove.next:
            temp = prev_remove.next.next
            prev_remove.next = None
            prev_remove.next = temp        
        
        return head
        
