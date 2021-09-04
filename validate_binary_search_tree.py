# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
INPUT
root of a bst

OUTPUT
is it valid
every node to the left has a value less than the current node
every node to the right has a value greater than the current node
both left and right are bst's

ALGORITHM
note: it is not enough to only check the current node and its children, we must maintain a state
recursive:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], floor: int, roof: int):
            # base case:
            # if tree is empty it meets the valid BST properties
            if not root:
                return True
            # ensure that that its value meets the conditions based on the rest of the tree
            if root.val <= floor or root.val >= roof:
                return False
            
            # recursive case:
            else:
                # left subtree is invalid
                if root.left and not helper(root.left, floor, min(root.val, roof)):
                    return False
                # right subtree is invalid
                if root.right and not helper(root.right, max(root.val, floor), roof):
                    return False
                # everything is invalid
                return True
                
                
            
        return helper(root, -float("inf"), float("inf"))

traversal
    
inorder: increasing -> left, root, right
IN -> INorder -> INcreasing
preorder: preordering root before increasing -> root, left, right
PREordering root before increasing order -> root, left, right

POSTorder: POSTordering root before increasing -> left, right, root
root is dying of boredom (POSTmortem) because it has to wait till end

root, left 
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case:
        # if tree is empty it meets the valid BST properties
        if not root:
            return True

        # node, floor, roof
        stack = [(root, -float("inf"), float("inf"))]

        while len(stack):
            curr = stack.pop()
            
            # ensure that that its value meets the conditions based on the rest of the tree
            if curr[0].val <= curr[1] or curr[0].val >= curr[2]:
                return False

            # recursive case:
            else:
                # add right
                if curr[0].right:
                    stack.append((curr[0].right, curr[0].val, curr[2]))
                
                # add left
                if curr[0].left:
                    stack.append((curr[0].left, curr[1], curr[0].val))
        
        return True
        
