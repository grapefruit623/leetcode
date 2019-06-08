# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        TLE
    '''
    def wordBreak(self, s: str, wordDict: List[str])->bool:
        l = len(s)
        self.dp = []
        for d in range(l):
            self.dp.append([False]*l)

        for i in range(0, l):
            for j in range(i, l):
                if s[i:j+1] in wordDict:
                    self.dp[i][j] = True
                
        return self.recWordBreak(s, wordDict, 0, 0)

    def recWordBreak(self, s, wd, i, j):
        if i >= len(s) or j >= len(s):
            return True

        for j in range(i, len(s)):
            if self.dp[i][j] == True:
                remain = self.recWordBreak(s, wd, j+1, j+1)
                if remain == True:
                    return True

        return False

class unittest_wordBreak(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        s = "leetcode"
        wordDict = {"leet", "code"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))
    
    def test_sample2(self):
        s = "applepenapple"
        wordDict = {"apple", "pen"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample3(self):
        s = "catsandog"
        wordDict = {"cats", "dop", "sand", "and", "cat"}
        expected = False
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample_TLE(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

if __name__ == "__main__":
    unittest.main()
