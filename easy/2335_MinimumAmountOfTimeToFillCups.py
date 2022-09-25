# -*- coding: utf-8 -*-
#! /usr/bin/python3

from typing import List
import unittest

class Solution:

    class PriorityQueue:
        def __init__(self, data):
            self.queue = sorted(data, reverse=True)

            while len(self.queue) > 0 and self.queue[-1] == 0:
                self.queue.pop(-1)

        @property
        def len(self):
            return len(self.queue)

        def pop2(self):
            if self.len == 0:
                return ()

            ret = () 
            if len(self.queue) >= 2:
                ret = (self.queue[0], self.queue[1])
                self.queue[0] -= 1
                self.queue[1] -= 1
            else:
                ret = (self.queue[0])
                self.queue[0] -= 1

            self.queue = sorted(self.queue, reverse=True)

            while len(self.queue) > 0 and self.queue[-1] == 0:
                self.queue.pop(-1)
            
            return ret

    '''
        Priority queue solution.
        Make practice to implement priority queue, so slowly.
    '''
    def fillCups(self, amount: List[int]) -> int:
        pq = self.PriorityQueue(amount)
        ans = 0

        while pq.len != 0:
            ret = pq.pop2()

            if ret != ():
                ans += 1
            
        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        amount = [1,4,2]
        expected = 4

        self.assertEqual(expected, self.sol.fillCups(amount))

    def test_case2(self):
        amount = [5,4,4]
        expected = 7

        self.assertEqual(expected, self.sol.fillCups(amount))

    def test_case3(self):
        amount = [5,0,0]
        expected = 5

        self.assertEqual(expected, self.sol.fillCups(amount))

if __name__ == "__main__":
    unittest.main()

