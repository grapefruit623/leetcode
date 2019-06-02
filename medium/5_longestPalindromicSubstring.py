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

        if len(s) == 1:
            return s

        ans = ''
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                p = self.findPartialPalindromic(s, i, j)
                if ans == '':
                    ans = p
                else:
                    if len(p) > len(ans):
                        ans = p

        return ans

    def findPartialPalindromic(self, s, start, end):
        palindromic = ''
        if end < start:
            return ''
        if end == start:
            return s[end]
        else:
            if (start+end+1) % 2 == 0:
                j = math.ceil( (start+end+1)/2 )
                i = j-1 

                while i >= start and j <= end:
                    if s[i] != s[j]:
                        if j-i > 1:
                            palindromic = s[i+1:j]
                        else:
                            palindromic = s[j]
                        break
                    i -= 1
                    j += 1
                else:
                    if s[i+1] == s[j-1]:
                        palindromic = s[start:end+1]
            else:
                middle = math.floor((start+end+1)/2)
                i = j = middle
                while i >= start and j <= end:
                    if s[i] != s[j]:
                        if j-i > 1:
                            palindromic = s[i+1:j]
                        else:
                            palindromic = s[j]
                        break
                    i -= 1
                    j += 1
                else:
                    if s[i+1] == s[j-1]:
                        palindromic = s[start:end+1]

            return palindromic

class Unittest_longestPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case0(self):
        data = "bab"
        expected = "bab"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case1(self):
        data = "ba"
        expected = "a"
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

    def test_case10(self):
        data = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"

        expected = ""
        self.assertEqual(expected, self.sol.longestPalindrome(data))
if __name__ == '__main__':
    unittest.main()
