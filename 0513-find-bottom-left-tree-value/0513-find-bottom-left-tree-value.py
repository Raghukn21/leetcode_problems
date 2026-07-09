class Solution:
    def findBottomLeftValue(self, root):
        from collections import deque
        
        queue = deque([root])
        result = root.val
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result