#-*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 != None and t2 != None:
            t1.val += t2.val
        elif t1 == None:
            return t2
        elif t2 == None:
            return t1

        if t1.left != None:
            if t2.left != None:
                self.mergeTrees(t1.left, t2.left)
        else:
            if t2.left != None:
                t1.left = t2.left

        if t1.right != None:
            if t2.right != None:
                self.mergeTrees(t1.right, t2.right)
        else:
            if t2.right != None:
                t1.right = t2.right
            
        return t1

class Unittest_mergeTrees(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_createBinaryTree(self):
        data = [3,4,5,5,4,None,7]
        tree = self.createBinaryTree(data)
        self.isTreeEqual(data, tree)

    def test_exampleWithoutNone(self):
        t1 = self.createBinaryTree([1,3,2])
        t2 = self.createBinaryTree([2,1,3])
        mergedTreeData = [3,4,5]

        result = self.sol.mergeTrees(t1, t2)
        self.isTreeEqual(mergedTreeData, result)

    def test_example1(self):
        t1 = self.createBinaryTree([1,3,2,5])
        t2 = self.createBinaryTree([2,1,3,None,4,None,7])
        mergedTreeData = [3,4,5,5,4,None,7]

        result = self.sol.mergeTrees(t1, t2)

        self.isTreeEqual(mergedTreeData, result)

    def test_emptyOneTree(self):
        t1 = self.createBinaryTree([1,2,3])
        t2 = self.createBinaryTree([None])
        mergedTreeData = [1,2,3]

        result = self.sol.mergeTrees(t1, t2)
        self.isTreeEqual(mergedTreeData, result)

    def tearDown(self):
        self.sol = None

    def createBinaryTree(self, data):
        if data is []:
            return None

        j = 0
        node = None
        dataLen = len(data)

        if data[0] == None: # Empty tree
            return None

        root = TreeNode(data[0])
        treeNodeList = [ root ]

        while treeNodeList != []:
            node = treeNodeList.pop(0)
            if node != None:
                if (2*j+1) < dataLen:
                    if data[2*j+1] != None:
                        node.left = TreeNode(data[2*j+1])
                        treeNodeList.append(node.left)
                    else:
                        node.left = None

                if (2*j+2) < dataLen:
                    if data[2*j+2] != None:
                        node.right = TreeNode(data[2*j+2])
                        treeNodeList.append(node.right)
                    else:
                        node.right = None
            j += 1

        return root

    def isTreeEqual(self, data, tree):
        treeNodeQueue = [tree]
        levelOrderOutput = []

        while treeNodeQueue != []:
            n = treeNodeQueue.pop(0)
            if n != None:
                levelOrderOutput.append(n.val)
                treeNodeQueue.append(n.left)
                treeNodeQueue.append(n.right)
            else:
                levelOrderOutput.append(None)
        
        dataLen = len(data)
        levelOrderOutput = levelOrderOutput[:dataLen] # filter leaf node's null pointer
        self.assertEqual(data, levelOrderOutput)

if __name__ == "__main__":
    unittest.main()
