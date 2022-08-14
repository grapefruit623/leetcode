# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjDict = {}
        for i in range(numCourses):
            adjDict[i] = []

        '''
            course <- pre1, pre2
            so if course not have pre, that is outer node in graph
        '''
        for pair in prerequisites:
            course, pre = pair[0], pair[1]
            adjDict[course].append(pre)

        return self.topologicalSort(numCourses, adjDict)

    def topologicalSort(self, numCourses, adjDict):
        leave = []
        ans = []

        for n in range(numCourses):
            if adjDict[n] == []:
                leave.append(n)

        while leave != []:
            outterNode = leave.pop()
            ans.append(outterNode)

            adjDict.pop(outterNode)

            for node in adjDict:
                if outterNode in adjDict[node]:
                    adjDict[node].remove(outterNode)

                    if adjDict[node] == []:
                        leave.append(node)

        '''
            Cycle
        '''
        if len(adjDict) != 0:
            return []

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        numCourses=2
        prerequisites=[[1,0]]
        expect = [0,1]

        self.assertEqual(expect, self.sol.findOrder(numCourses, prerequisites))
    
    def test_case2(self):
        numCourses=4
        prerequisites=[[1,0],[2,0],[3,1],[3,2]]
        expect = [0,2,1,3]

        self.assertEqual(expect, self.sol.findOrder(numCourses, prerequisites))

    def test_case3(self):
        numCourses=1
        prerequisites=[]
        expect = [0]

        self.assertEqual(expect, self.sol.findOrder(numCourses, prerequisites))

    def test_case4(self):
        numCourses=3
        prerequisites=[[1,0], [1,2], [0,1]]
        expect = []

        self.assertEqual(expect, self.sol.findOrder(numCourses, prerequisites))

if __name__ == "__main__":
    unittest.main()

