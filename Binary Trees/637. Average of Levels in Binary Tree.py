from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []

        d = deque()
        d.append(root)

        while d:
            avg = 0
            n = len(d)
            for _ in range(n):
                node = d.popleft()
                avg += node.val

                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
            
            avg /= n
            avgs.append(avg)
        
        return avgs
        # Time: O(n)
        # Space: O(n)