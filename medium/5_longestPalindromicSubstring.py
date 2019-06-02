#! -*- coding:utf-8 -*-
import unittest
import math

class Solution:
    '''
        TLE
    '''
    def longestPalindrome(self, s:str)->str:
        if s is None:
            return None

        length = len(s)
        if length == 1:
            return s

        ans = ''
        for i in range(0, length):
            for j in range(i+1, length):
                p = self.findPartialPalindromic(s, i, j)
                if len(p) > len(ans):
                    ans = p

        return ans

    def findPartialPalindromic(self, s, start, end):
        if end == start:
            return s[end]
        else:
            i = j = 0
            if (start+end+1) % 2 == 0:
                j = math.ceil( (start+end+1)/2 )
                i = j-1 
            else:
                i = j = math.floor((start+end+1)/2)

            while i >= start and j <= end and s[i] == s[j]:
                i -= 1
                j += 1

            if j-i > 1:
                return s[i+1:j]
            else:
                return s[i:j]

class Unittest_longestPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case0(self):
        data = "bab"
        expected = "bab"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case1(self):
        data = "ba"
        expected = "b"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case3(self):
        data = "babad"
        expected = "bab"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case4(self):
        data = "cbbd"
        expected = "bb"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case5(self):
        data = "c"
        expected = "c"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case6(self):
        data = ""
        expected = ""
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case7(self):
        data = None 
        expected = None 
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case8(self):
        data = "abadd" 
        expected = "aba" 
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case9(self):
        data = "eabcb" 
        expected = "bcb" 
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    '''
    def test_case10(self):
        data = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"

        expected = ""
        self.assertEqual(expected, self.sol.longestPalindrome(data))
    '''
if __name__ == '__main__':
    unittest.main()
