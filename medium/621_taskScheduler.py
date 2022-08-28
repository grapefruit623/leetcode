# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int)->int:
        if n == 0:
            return len(tasks)

        idleMark = 'I'
        ansSeq = []
        hashTable = {}

        for t in tasks:
            if t not in hashTable:
                hashTable[t] = 1
            else:
                hashTable[t] += 1

        sortedData = sorted(hashTable.items(), key=lambda x:x[1], reverse=True)
        maxFreq = sortedData[0][1]

        ansSeq=[idleMark]*(maxFreq+maxFreq*n)
        
        startPos = 0
        for data in sortedData:
            task, count = data[0], data[1]
            for c in range(count):
                ansSeq[startPos+c*(n+1)] = task
            startPos += 1

        while ansSeq[-1] == idleMark:
            ansSeq.pop(-1)
        
        return len(ansSeq)

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        tasks=['A','A','A','B','B','B']
        n = 2
        expect = 8
        self.assertEqual(expect, self.sol.leastInterval(tasks, n)) 

    def test_case2(self):
        tasks=['A','A','A','B','B','B']
        n = 0
        expect = 6
        self.assertEqual(expect, self.sol.leastInterval(tasks, n)) 
        
    def test_case3(self):
        tasks =[ "A","A","A","A","A","A","B","C","D","E","F","G"] 
        n = 2
        expect = 16
        self.assertEqual(expect, self.sol.leastInterval(tasks, n)) 

if __name__ == "__main__":
    unittest.main()
