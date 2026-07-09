class Solution:
    def findFrequentTreeSum(self, root):
        from collections import defaultdict
        
        count = defaultdict(int)
        
        def subtreeSum(node):
            if not node:
                return 0
            left = subtreeSum(node.left)
            right = subtreeSum(node.right)
            total = node.val + left + right
            count[total] += 1
            return total
        
        subtreeSum(root)
        
        max_freq = max(count.values())
        return [s for s, freq in count.items() if freq == max_freq]