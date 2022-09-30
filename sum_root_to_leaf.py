#time complexity:o(n) where n is elements of bin tree
#space complexity:o(h) where h is height of bin tree
#passed all cases on LeetCode: yes
#difficulty faced:
# comments:in the code
#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: 'Optional[TreeNode]') -> int:

        self.totsum = 0

        
        def dfs(root, num: int) -> None:

            if root == None:
                return
            #when we reach leaf (last child) add to the sum 
            if root.left == None and root.right == None:
                self.totsum += num*10+root.val 
            #we have to multiply only by 10 everytime
            dfs(root.left,num*10+root.val)
            dfs(root.right,num*10+root.val)
        
        if root == None:
            return 0
        dfs(root,0)
        return self.totsum