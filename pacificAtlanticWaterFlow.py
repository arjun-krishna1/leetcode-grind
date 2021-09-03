'''
GIVEN
INPUT
heights: m x n integer matrix
height above sea level at coordinate (r, c)
borders both the Pacific Ocean and Atlantic Ocean
Pacific Ocean touches the left and top edges
Atalantic Ocean touches the right and bottom edges
rain water can flow to neighboring cells directly north, south, east, and west
    if the neighboring cell's height is less than or equal to the current cell's height
    water can flow from any cell adjacent to an ocean into the ocean
    
OUTPUT
result: 2d list of grid coordinates
result[i] - [ri, ci] donates that rain can flow from (ri, ci) to both the Pacific and Atlantic oceans

ALGORITHM
create a stack
create hashmap
    key is coordinate tuple
    value represents it gets water from Pacific Ocean
    defaultdict returns False when not visited
add all elements bordering top and left to stack
while stack is not empty
    get this node from stack
    get all coordinates that water can flow into from this node and are not in hashmap
    mark these nodes as recieveing pacific ocean water
    add them to stack
    
repeat above with a new hashmap and bottom and right

get all coordinates that are True in both hashmaps and add to result

return result
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(heights)
        n = len(heights[0])
        
        def get_nodes_connected(visited_map, to_visit):
            while len(to_visit):
                curr = to_visit.pop()

                for d in dirs:
                    # get this new node location
                    new_i = curr[0] + d[0]
                    new_j = curr[1] + d[1]

                    # visit this node if it is within the island
                    flows = 0 <= new_i < m and 0 <= new_j < n
                    
                    # also if water can flow from new node to this current node
                    flows = flows and heights[new_i][new_j] >= heights[curr[0]][curr[1]]
                    
                    # and it hasn't been visited yet
                    flows = flows and not ((new_i, new_j) in visited_map and visited_map[(new_i, new_j)])
                    
                    # if we should visit it
                    if flows:
                        # mark it as visited
                        visited_map[(new_i, new_j)] = True
                        # add its node to the stack
                        to_visit.append((new_i, new_j))
            
            return visited_map
        
        pacific = {}
        stack = []
        
        # all nodes in the top and left flow into the pacific ocean
        # left side
        for i in range(m):
            pacific[(i, 0)] = True
            stack.append((i, 0))
            
        # top side
        for j in range(1, n):
            pacific[(0, j)] = True
            stack.append((0, j))

        # use dfs to get all nodes that flow into the pacific ocean
        pacific = get_nodes_connected(pacific, stack)
        
        atlantic = {}
        stack = []
        
        # all nodes in the bottom and right flow into the atlantic ocean
        # right
        for i in range(m):
            atlantic[(i, n - 1)] = True
            stack.append((i, n - 1))
            
        # bottom
        for j in range(n - 1):
            atlantic[(m - 1, j)] = True
            stack.append((m - 1, j))
            
        # use dfs to get all nodes that flow into the atlantic ocean
        atlantic = get_nodes_connected(atlantic, stack)
            
        result = []
        for i in range(m):
            for j in range(n):
                # if water from this node flows into the pacific and atlantic ocean
                flows_to_both = (i, j) in pacific and pacific[(i, j)]
                flows_to_both = (i, j) in atlantic and atlantic[(i, j)] and flows_to_both
                
                if flows_to_both:
                    result.append((i, j))
                    
        return result
      
