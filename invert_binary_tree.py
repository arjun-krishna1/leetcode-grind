# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
INPUT
root of btree

OUTPUT
btree that is inverted
flipped in a mirror

ALGORITHM
RECURSIVE
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # swap left and right subtrees
            root.left, root.right = root.right, root.left
            # recursively invert the left and right subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        
ITERATIVE pre-order traversal (root, left, right)
create a stack with only root
while stack is not empty
    pop curr from stack
    swap left and right
    add left and right to stack
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        stack = [root]
        
        while len(stack):
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root
            
