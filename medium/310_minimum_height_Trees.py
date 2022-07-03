# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC more faster and my style
    '''
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        directGraph = { i:[] for i in range(n)}

        '''
            Adjanency matrix
        '''
        for e in edges:
            directGraph[ e[0] ].append(e[1])
            directGraph[ e[1] ].append(e[0])

        '''
            Use Topological sort
        '''

        leaveNode = []

        while len(directGraph) > 2:# Because there can be two roots have same height
            '''
                First time
            '''
            if leaveNode == []:
                for node in directGraph.keys():
                    '''
                        Only one connection means leaf
                    '''
                    if len(directGraph[node]) == 1:
                        leaveNode.append(node)

            nextLeaveNode = []
            for lNode in leaveNode:
                parentNode = directGraph[lNode][0]
                directGraph[parentNode].remove(lNode)
                directGraph.pop(lNode)

                if len(directGraph[parentNode]) == 1:
                    nextLeaveNode.append(parentNode)


            leaveNode = nextLeaveNode

        return [ node for node in directGraph ]

    '''
        AC, but slowly
    '''
    def findMinHeightTrees_slow(self, n: int, edges: List[List[int]]) -> List[int]:

        directGraph = { i:[] for i in range(n)}
        
        '''
            Adjanency matrix
        '''
        for e in edges:
            directGraph[ e[0] ].append(e[1])
            directGraph[ e[1] ].append(e[0])
        
        '''
            Use Topological sort
        '''
        
        leaveNode = []
        
        for i in range(n):
            '''
                Only one connection means leaf
            '''
            if i in directGraph.keys() and len(directGraph[i]) == 1:
                leaveNode.append(i)
        
        while len(directGraph) > 2:# Because there can be two roots have same height
            nextLeave = []
            for lNode in leaveNode:
                parentNode = directGraph[lNode][0]
                directGraph[parentNode].remove(lNode)
                directGraph.pop(lNode)
                '''
                    The node which connect to leaf will become next generation of leaves when leaf node removed.
                '''
                if parentNode not in nextLeave and len(directGraph[parentNode]) == 1:
                    nextLeave.append(parentNode)

            
            leaveNode = nextLeave
            
        return [ node for node in directGraph ]

    def findMinHeightTrees_tle2(self, n: int, edges: List[List[int]]) -> List[int]:
        directGraph = { i:[] for i in range(n)}

        '''
            Adjanency matrix
        '''
        for e in edges:
            directGraph[ e[0] ].append(e[1])
            directGraph[ e[1] ].append(e[0])

        '''
            Use Topological sort
        '''

        leaveNode = []

        while len(directGraph) > 2:# Because there can be two roots have same height
            for i in range(n):
                '''
                    Only one connection means leaf
                '''
                if i in directGraph.keys() and len(directGraph[i]) == 1:
                    leaveNode.append(i)


            for lNode in leaveNode:
                parentNode = directGraph[lNode][0]
                directGraph[parentNode].remove(lNode)
                directGraph.pop(lNode)


            leaveNode = []

        return [ node for node in directGraph ]


    def findMinHeightTrees_tle1(self, n: int, edges: List[List[int]]) -> List[int]:
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
