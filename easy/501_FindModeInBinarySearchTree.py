# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
        AC
    """
    def findMode(self, root:TreeNode)->List[int]:
        freqDict = {}
        bfsQueue = []
        ans = []
        maxFreqCount = -1
        
        if root == None:
            return []

        bfsQueue.append(root)

        while bfsQueue != []:
            node = bfsQueue.pop()
            freqDict[node.val] = freqDict.get(node.val, 0)+1
            maxFreqCount = max(maxFreqCount, freqDict[node.val])

            if node.left != None:
                bfsQueue.append(node.left)
            if node.right != None:
                bfsQueue.append(node.right)

        for k,v in freqDict.items():
            if v == maxFreqCount:
                ans.append(k)

        return ans

class Unittest_findMode(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_sample1(self):
        root = TreeNode(1)
        root.left = None
        root.right = TreeNode(2)
        root.right.left = TreeNode(2)
        expected = [2]
        self.assertEqual(expected, self.sol.findMode(root))
        
if __name__ == "__main__":
    unittest.main()
