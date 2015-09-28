#! /usr/bin/python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

'''
    Must to using in-place algorithm
    refer: https://zh.wikipedia.org/wiki/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95
'''


class Solution(object):
    def flatten(self, root):
        self.flattenedList = []
        self.dfs(root)
        treeLen = xrange(len(self.flattenedList)-1)
        for i in treeLen:
            self.flattenedList[i].right = self.flattenedList[i+1]
            self.flattenedList[i].left = None
        root = self.flattenedList[0]

    def dfs(self, root):
        self.flattenedList.append(root)
        if root is not None:
            if root.left is not None:
                self.dfs(root.left)
            if root.right is not None:
                self.dfs(root.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)

    l = TreeNode(2)
    l.left = TreeNode(3)
    l.right = TreeNode(4)

    r = TreeNode(5)
    r.right = TreeNode(6)

    root.left = l
    root.right = r

    s.flatten(root)
