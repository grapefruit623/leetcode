#! /usr/bin/python3
# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "[{0} {1} {2}]".format(self.val, self.left, self.right)

'''
    AC
'''
class Solution(object):
    def pruneTree(self, root):
        self.root = root
        return self.pruneDfs(root)

    def pruneDfs(self, currentNode):
        if currentNode == None:
            return None

        currentNode.left = self.pruneDfs(currentNode.left)
        currentNode.right = self.pruneDfs(currentNode.right)

        if currentNode.left == None and currentNode.right == None and currentNode.val == 0:
            return None
        else:
            return currentNode

def dfs(root):
    if root == None:
        return 
    if root.val == None:
        print (None)

    dfs(root.left)
    dfs(root.right)
    print (root.val)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    dfs(root)
    print ('-'*30)
    dfs(sol.pruneTree(root))

    
