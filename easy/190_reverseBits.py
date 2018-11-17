# -*- coding:utf-8 -*-
#! /usr/bin/pyhon3
import unittest

"""
    AC
"""
class Solution(object):
    def reverseBits(self, n):
        binNum = bin(n)[2:].zfill(32)
        ans = 0

        for i in range(32):
            if binNum[i] == '1':
                ans += 2**i
        return ans

class Unittest_reverseBits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = 43261596
        expected = 964176192
        self.assertEqual(expected, self.sol.reverseBits(data))

    def tearDown(self):
        self.sol = None
if __name__ == "__main__":
    unittest.main()
