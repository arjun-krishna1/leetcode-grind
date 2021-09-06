
'''
it is impossible to finish all courses
if there is some set of courses that has a cyclical prerequisite
for example 1 requires 2 requires 3 requires 1
given the number of nodes
and the adjacency matrix of the graph
return whether it is acyclical or not

TOPOLOGICAL SORT!!!!

ALGORITHM
create a hashmap of sets
    key is a node
    value is a set of nodes it is connected to
    

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:       
        # hashmap where key is a course
        # and value is all the nodes that can be taken once the key is finished
        child_map = {}
        for i in range(numCourses):
            child_map[i] = set()
            
        for i in prerequisites:
            child_map[i[1]].add(i[0])
            
        # nodes we still have to visit
        unmarked_nodes = set([i for i in range(numCourses)])
        
        # set to hold marked nodes for cycle detection
        perm = set()
        temp = set()
        
        def check_cycle(node: int) -> bool:
            # if it has already been checked for a cycle
            # and it didn't have a cycle
            if node in perm:
                return True
            
            # if this course was being checked for cycles
            # and we are here already
            # there is a cycle
            elif node in temp:
                return False
            
            # remove this node from being  considered in the future
            if node in unmarked_nodes:
                unmarked_nodes.remove(node)
            
            # mark this node  as being visited
            temp.add(node)
            
            # go through all the courses that need it
            for child in child_map[node]:
                # check for a cycle
                no_cycle = check_cycle(child)
                # if there is a cycle return false
                if not no_cycle:
                    return False
                
            # this course is no longer being visited
            temp.remove(node)
            
            # this node has been checked for a cycle and it has no cycles
            perm.add(node)
            
            return True
        
        # while we have more nodes to check
        while len(perm) < numCourses:
            # get a random unchecked node
            curr = unmarked_nodes.pop()
            # if it is in a cycle return False
            if not check_cycle(curr):
                return False
            
        # if all of its nodes are not in a cycle
        # this node has no cycles
        # the courses can be completed
        return True
        
