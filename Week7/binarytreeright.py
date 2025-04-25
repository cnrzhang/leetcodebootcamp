# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        level = [root]
        while level:
            temp = []
            result.append(level[-1].val)

            for i in level:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            
            level = temp.copy()

        return result