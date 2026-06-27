class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {}  # maps original node -> its clone

        def dfs(original):
            # If we've already cloned this node, return the existing clone
            # (this is what prevents infinite loops on cycles)
            if original in visited:
                return visited[original]

            # Create the clone and register it immediately,
            # BEFORE recursing into neighbors
            clone = Node(original.val)
            visited[original] = clone

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)