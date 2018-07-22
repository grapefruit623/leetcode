# -*- coding: utf-8 -*-
#! /usr/bin/python3

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    """
        AC and easy to AC.
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype List[List[int]]
        """
        if root == None:
            return []

        queue = []
        ans = []

        queue.append( (root,0) )

        while len(queue) != 0:
            (node, level) = queue.pop(0)

            if len(ans) < level+1:
                ans.append([])

            ans[level].append(node.val)

            if node.left != None:
                queue.append( (node.left, level+1) )
            if node.right != None:
                queue.append( (node.right, level+1) )

        return ans

