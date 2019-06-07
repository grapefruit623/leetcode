#! -*- coding:utf-8 -*-
import unittest
import math

class Solution:
    '''
        DP
    '''
    def longestPalindrome(self, s:str)->str:
        if s == None:
            return None

        if s == '':
            return ''

        dp = []
        l = len(s)
        for i in range(l):
            dp.append([False]*l)
            dp[i][i] = True

        ans = s[0] 
        maxLen = 1
        for i in range(l-1, -1, -1):
            for j in range(l-1, i, -1):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i > 1:
                        if dp[i+1][j-1] == True:
                            dp[i][j] = True
                            if j-i+1 > maxLen:
                                ans = s[i:j+1]
                                maxLen = len(ans)
                    else:
                        dp[i][j] = True
                        if j-i+1 > maxLen:
                            ans = s[i:j+1]
                            maxLen = len(ans)
        return ans
    '''
        TLE
    '''
    def longestPalindrome_TLE(self, s:str)->str:
        if s is None:
            return None

        length = len(s)
        if length == 1:
            return s

        ans = ''
        maxLen = 0
        for i in range(0, length):
            for j in range(i+1, length):
                p = self.findPartialPalindromic(s, i, j)
                currLen = len(p)
                if currLen > maxLen:
                    ans = p
                    maxLen = currLen

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
        expected = "aba"
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

        expected = "I don't know correct answear"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case11(self):
        data = "abcda"
        expected = "a"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

    def test_case11(self):
        data = "aaaa"
        expected = "aaaa"
        self.assertEqual(expected, self.sol.longestPalindrome(data))

if __name__ == '__main__':
    unittest.main()
