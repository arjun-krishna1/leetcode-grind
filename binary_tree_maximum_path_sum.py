# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumHelper(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return [-float("inf"), -float("inf")]
            
            lpath = maxPathSumHelper(root.left)
            rpath = maxPathSumHelper(root.right)
            
            res = [0, 0]
            #print(lpath, rpath)
            # maximum of any paths ending on this root node
            # these paths can be extended by partent
            res[1] = max(root.val, lpath[1] + root.val, rpath[1] + root.val)
            # maximum of any paths in this subtree
            # these paths may not be extended by a parent
            res[0] = max(res[1], lpath[1] + rpath[1] + root.val, lpath[0], rpath[0])
            
            return res
        
        return maxPathSumHelper(root)[0]
