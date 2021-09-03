'''
GIVEN
INPUT
m by n 2D binary grid grid
represents a map of '1's (land) and '0's (water)

OUTPUT
return the number of islands
island is surrounded by water
formed by connecting adjacent lands horizontally or vertically
assume all four edges of the grid are all surrounded by water

ALGORITHM
BREADTH FIRST SEARCH
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
m = len(grid)
n = len(grid[0])

def remove_island(i, j):
    # store nodes to remove and consider neighbors of
    stack = [(i, j)]
    while len(stack):
        # get this node
        curr = stack.pop()
        # ignore this land from here on
        grid[curr[0]][curr[1]] = "0"
        for dir in dirs:
            # get this new node location
            new_i = curr[0] + dir[0]
            new_j = curr[1] + dir[1]
            # if this new node location is within the map
            if 0 <= new_i < m and 0 <= new_j < n:
                # add it to stack
                stack.append((new_i, new_j))
                
        
num_islands = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "1":
            num_islands += 1
            remove_island(i, j)
return num_islands

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        num_loops = 0
        def remove_island(i, j):
            # store nodes to remove and consider neighbors of
            stack = [(i, j)]
            while len(stack):
                # get this node
                curr = stack.pop()
                # ignore this land from here on
                grid[curr[0]][curr[1]] = "0"
                for dir in dirs:
                    # get this new node location
                    new_i = curr[0] + dir[0]
                    new_j = curr[1] + dir[1]
                    # if this new node location is within the map
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1":
                        # add it to stack
                        stack.append((new_i, new_j))

        num_islands = 0
        # iterate through entire grid
        for i in range(m):
            for j in range(n):
                # if this is a part of an island
                if grid[i][j] == "1":
                    # increase the number of islands
                    num_islands += 1
                    # ignore it here on out
                    remove_island(i, j)
        return num_islands
        
