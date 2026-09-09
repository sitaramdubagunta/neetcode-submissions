"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        map1 = defaultdict(list)

        def dfs(node):

            if not node:
                return 
            if node in map1:
                return map1[node]
            copy = Node(node.val)
            map1[node] = copy
            
            for nei in node.neighbors:
                
                    copy.neighbors.append(dfs(nei))


            return copy

        return dfs(node)
