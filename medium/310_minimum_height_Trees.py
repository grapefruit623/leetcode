# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
            Store n node with height
        '''
        treeTable = [-1]*n

        directGraph = { i:[] for i in range(n)}

        for e in edges:
            directGraph[ e[0] ].append(e[1])
            directGraph[ e[1] ].append(e[0])

        self.minHeight = n+1

        for i in range(n):
            isVisited = [False]*n
            mht = self.dfs(i, 0, directGraph, isVisited)
            treeTable[i] = mht
            self.minHeight = min(self.minHeight, mht)

        ans = []
        for n in range(len(treeTable)):
            if treeTable[n] == self.minHeight:
                ans.append(n)

        return ans

    def dfs(self, root, height, directGraph, isVisited):
        isVisited[root] = True
        maxHeight = height
        for node in directGraph[root]:
            if isVisited[node] == False:
                maxHeight = max(maxHeight, self.dfs(node, height+1, directGraph, isVisited))

                if maxHeight > self.minHeight:
                    return maxHeight

        isVisited[root] = False
        return maxHeight

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n=4
        edge=[[1,0],[1,2],[1,3]]
        expect = [1]
        self.assertEqual(expect, self.sol.findMinHeightTrees(n, edge))

if __name__ == "__main__":
    unittest.main()
