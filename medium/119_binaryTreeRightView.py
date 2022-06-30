#! -*-coding: utf-8 -*-
#! /usr/bin/python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        AC
        ref: https://www.cnblogs.com/grandyang/p/4392254.html
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        ans = []
        queue = []

        queue.append(root)
        self.r_bfs_helper(queue, ans)

        return ans

    def r_bfs_helper(self, queue, ans):
        while queue != []:
            n = queue[0]
            ans.append(n.val)

            l = len(queue)
            for i in range(l):
                n = queue.pop(0)

                if n.right != None:
                    queue.append(n.right)
                if n.left != None:
                    queue.append(n.left)

if __name__ == "__main__":
    pass
