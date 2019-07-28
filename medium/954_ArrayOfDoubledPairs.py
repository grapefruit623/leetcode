# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def canReorderDoubled(self, A:List[int])->bool:
        hashTable = {}
        A.sort()

        for a in A:
            if a not in hashTable:
                hashTable[a] = 1
            else:
                hashTable[a] += 1

            half = a/2
            if half in hashTable and hashTable[half] > 0 and hashTable[a] > 0:
                hashTable[half] -= 1
                hashTable[a] -= 1

            double = a*2
            if double in hashTable and hashTable[double] > 0 and hashTable[a] > 0:
                hashTable[double] -= 1
                hashTable[a] -= 1
            
        return True if sum(hashTable.values()) == 0 else False
                

class unittest_canReorderDoubled(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [3,1,3,6]
        self.assertEqual(False, self.sol.canReorderDoubled(data))

    def test_sample2(self):
        data = [2,1,2,6]
        self.assertEqual(False, self.sol.canReorderDoubled(data))

    def test_sample3(self):
        data = [4,-2,2,-4]
        self.assertEqual(True, self.sol.canReorderDoubled(data))

    def test_sample4(self):
        data = [1,2,4,16,8,4]
        self.assertEqual(False, self.sol.canReorderDoubled(data))

    def test_sample5(self):
        data = [1,2]
        self.assertEqual(True, self.sol.canReorderDoubled(data))

    def test_sampleWA1(self):
        data = [0,0]
        self.assertEqual(True, self.sol.canReorderDoubled(data))

    def test_sampleWA2(self):
        data = [7,-15,-15,23,-3,80,-35,40,68,22,44,98,20,0,-34,8,40,41,16,46,16,49,-6,-11,35,-15,-74,72,-8,60,40,-2,0,-6,34,14,-16,-92,54,14,-68,82,-30,50,22,25,16,70,-1,-96,11,45,54,40,92,-35,29,80,46,-30,27,7,-70,-37,41,-46,-98,1,-33,-24,-86,-70,80,-43,98,-49,30,0,27,2,82,36,0,-48,3,-100,58,32,90,-22,-50,-12,36,6,-3,-66,72,8,49,-30]
 
        self.assertEqual(True, self.sol.canReorderDoubled(data))

if __name__ == '__main__':
    unittest.main()
