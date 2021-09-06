"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        # create a deep copy of the input node with no neighbors and add to hashmap
        node_copies = {node: Node(node.val)}
        
        stack = []
        # add node's neighbors to hashmap and mark them to be visited
        for n in node.neighbors:
            node_copies[n] = Node(n.val)
            stack.append(n)
            node_copies[node].neighbors.append(node_copies[n])
            
        # while we have more nodes to visit
        while len(stack):
            # get the original node who's copies neighbors we want to add
            curr = stack.pop()
            
            # iterate through each of the original node's neighbors
            for n in curr.neighbors:
                # if this is a new node we haven't seen, create a copy for it
                # and remember it so we can visit it later
                if n not in node_copies:
                    node_copies[n] = Node(n.val)
                    stack.append(n)
                
                # add this neighbors copy to curr's copies neighbors
                node_copies[curr].neighbors.append(node_copies[n])
                
        # return the copy of the original node
        return node_copies[node]
