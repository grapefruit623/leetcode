#! -*-coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution(object):
    def isPalindrome(self, x: int)->bool:
        if x < 0:
            return False

        s = str(x)
        i = 0
        j = len(s)-1 

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

class unittest_isPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sampel1(self):
        data = 121
        self.assertEqual(True, self.sol.isPalindrome(data))

    def test_sampel2(self):
        data = -121
        self.assertEqual(False, self.sol.isPalindrome(data))

    def test_sampel3(self):
        data = 10 
        self.assertEqual(False, self.sol.isPalindrome(data))

    def test_sampel4(self):
        data = 0 
        self.assertEqual(True, self.sol.isPalindrome(data))

if __name__ == '__main__':
    unittest.main()
