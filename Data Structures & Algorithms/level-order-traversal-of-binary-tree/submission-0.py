# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        result = []
        queue.append(root)
        
        level = 0
        while len(queue) > 0:
            inCurrent = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    inCurrent.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if inCurrent:
                result.append(inCurrent)
            level += 1
        return result
    